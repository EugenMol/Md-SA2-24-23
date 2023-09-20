#!/usr/bin/env python3
import json
import signal
import sys
import time
from influxdb import InfluxDBClient
from redis import Redis
from datetime import datetime, timedelta
from loguru import logger
from decouple import config
redis_host = config('REDIS_HOST')
redis_port = config('REDIS_PORT', default=6379, cast=int)
influxdb_host = config('INFLUXDB_HOST')
influxdb_port = config('INFLUXDB_PORT', default=8086, cast=int)
influxdb_username = config('INFLUXDB_USERNAME')
influxdb_password = config('INFLUXDB_PASSWORD')
influxdb_database = config('INFLUXDB_DATABASE')
redis_channel = config('REDIS_CHANNEL')
redis_client = Redis(host=redis_host, port=redis_port)
influx_client = InfluxDBClient(influxdb_host, influxdb_port, influxdb_username, influxdb_password, influxdb_database)
logger.add("logs/app.log", rotation="0.01 MB", colorize=True, format="{time} {level} {message}")
if redis_client.ping():
    logger.info('Успешно подключено к Redis')
else:
    logger.error('Ошибка подключения к Redis')
if influx_client.ping():
    logger.info('Успешно подключено к InfluxDB')
else:
    logger.error('Ошибка подключения к InfluxDB')


def get_data_from_redis():
    while True:
        redis_list = redis_client.lrange('dbwrite', 0, -1)
        for redis_record in redis_list:
            redis_record_json = json.loads(redis_record)
            measurement = redis_record_json['command']
            vm_id = redis_record_json['vmid']
            data = redis_record_json['data']
            transformed_data = data.copy()
            if redis_record_json['command'] == 'min30all':
                min30date = redis_record_json['date']
                for redis_record_json in data:
                    def index_time(index):
                        hours = (index - 1) // 2
                        minutes = 30 if index % 2 == 0 else 00
                        return f"{hours:02}:{minutes:02}"

                    for key in ['pp', 'pm', 'qp', 'qm']:
                        if redis_record_json[key] is None or redis_record_json[key] == 0:
                            redis_record_json[key] = 0.0
                        else:
                            redis_record_json[key] = float(redis_record_json[key])
                    date_string = f"{min30date}T{index_time(redis_record_json['index'])}:00"
                    datetime_format = "%Y-%m-%dT%H:%M:%S"
                    datetime_obj = datetime.strptime(date_string, datetime_format)
                    utc_offset = timedelta(hours=2.5)
                    datetime_obj_utc3 = datetime_obj - utc_offset
                    json_data = [
                        {
                            "measurement": measurement,
                            "tags": {
                                "vm:id": vm_id
                            },
                            "time": datetime_obj_utc3,
                            "fields": {
                                "pp": redis_record_json['pp'],
                                "pm": redis_record_json['pm'],
                                "qp": redis_record_json['qp'],
                                "qm": redis_record_json['qm']
                            }

                        }
                    ]
                    influx_client.write_points(json_data)
                logger.info(f'Record add to Influx:{redis_record}')
                redis_client.lrem('dbwrite', 1, redis_record)
                logger.info(f'Record deleted from redis:{redis_record}')

            elif redis_record_json['command'] == 'day' or redis_record_json['command'] == 'incday':
                tarif = redis_record_json['data']['tarif']
                for key in ['em', 'ep', 'rp', 'rm']:
                    if key in transformed_data:
                        value = transformed_data[key]
                        if value is None or value == 0:
                            transformed_data[key] = 0.0
                        else:
                            transformed_data[key] = float(value)

                date_string = f"{redis_record_json['data']['date']}T{redis_record_json['data']['time']:00}"
                datetime_format = "%Y-%m-%dT%H:%M:%S"
                datetime_obj = datetime.strptime(date_string, datetime_format)
                utc_offset = timedelta(hours=3)
                datetime_obj_utc3 = datetime_obj - utc_offset
                json_data = [
                    {
                        "measurement": measurement,
                        "tags": {
                            "tags": vm_id,
                            "tarif": tarif
                        },
                        "time": datetime_obj_utc3,
                        "fields": transformed_data
                    }
                ]
                influx_client.write_points(json_data)
                logger.info(f'Record add to Influx:{redis_record}')
                redis_client.lrem('dbwrite', 1, redis_record)
                logger.info(f'Record deleted from redis:{redis_record}')
            elif redis_record_json['command'] == 'instant':
                time.sleep(1)
                current_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
                transformed_data = redis_record_json.copy()
                for key, value in transformed_data['data'].items():
                    if key != 'date' and key != 'time':
                        if key != 'command' and (value is None or value == 0):
                            transformed_data['data'][key] = 0.0
                        else:
                            transformed_data['data'][key] = float(value)
                json_data = [
                    {
                        "measurement": measurement,
                        "tags": {
                            "vm_id": vm_id
                        },
                        "time": current_time,
                        "fields": {
                            "command": transformed_data['command'],
                            "power_active": transformed_data['data']['power_active'],
                            "power_active_phase_a": transformed_data['data']['power_active_phase_a'],
                            "power_active_phase_b": transformed_data['data']['power_active_phase_b'],
                            "power_active_phase_c": transformed_data['data']['power_active_phase_c'],
                            "power_reactive": transformed_data['data']['power_reactive'],
                            "power_reactive_phase_a": transformed_data['data']['power_reactive_phase_a'],
                            "power_reactive_phase_b": transformed_data['data']['power_reactive_phase_b'],
                            "power_reactive_phase_c": transformed_data['data']['power_reactive_phase_c'],
                            "voltage": transformed_data['data']['voltage'],
                            "voltage_phase_a": transformed_data['data']['voltage_phase_a'],
                            "voltage_phase_b": transformed_data['data']['voltage_phase_b'],
                            "voltage_phase_c": transformed_data['data']['voltage_phase_c'],
                            "amperage_phase_a": transformed_data['data']['amperage_phase_a'],
                            "amperage_phase_b": transformed_data['data']['amperage_phase_b'],
                            "amperage_phase_c": transformed_data['data']['amperage_phase_c'],
                            "frequency": transformed_data['data']['frequency'],
                            "power_coeff_phase_a": transformed_data['data']['power_coeff_phase_a'],
                            "power_coeff_phase_b": transformed_data['data']['power_coeff_phase_b'],
                            "power_coeff_phase_c": transformed_data['data']['power_coeff_phase_c']
                        }
                    }
                ]
                influx_client.write_points(json_data)
                logger.info(f'Record add to Influx:{redis_record}')
                redis_client.lrem('dbwrite', 1, redis_record)
                logger.info(f'Record deleted from redis:{redis_record}')
            else:
                logger.warning(f'Skipping message with unknown command: {redis_record_json["command"]}')
                redis_client.lrem('dbwrite', 1, redis_record)
                continue
        time.sleep(1)


def signal_handler(sig, frame):
    logger.error('Приложение завершено')
    sys.exit(0)


if __name__ == '__main__':
    try:
        logger.info('Приложение запущено')
        signal.signal(signal.SIGINT, signal_handler)
        get_data_from_redis()
    except Exception as e:
        logger.error(f'Произошла ошибка: {e}')
