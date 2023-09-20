import json
import os
from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from starlette import status
from Channel.channel_delete import channel_remove
from Channel.all_channels_get import get_all_channels
from Channel.current_channel_get import get_channel_by_id
from Channel.channel_post import channel_add
from Channel.channel_put import channel_update
from Excel.channel_excel import channel_excel
from Excel.group_excel import group_excel
from Excel.meter_excel import meter_excel
from Groups.group_delete import group_remove
from Groups.all_groups_get import get_all_groups
from Groups.current_group_get import get_group_by_id
from Groups.group_post import group_add
from Groups.group_put import group_update
from Meter.meter_delete import meter_remove
from Meter.all_meters_get import get_all_documents
from Meter.current_meter_get import get_document_by_id
from Meter.meter_post import meter_add
from Meter.meter_put import meter_update
from Models.channel import Channel
from Models.group import Group
from Models.meter import Meter
from fastapi.middleware.cors import CORSMiddleware
from settings import db, groups_collection, meters_collection, channels_collection

templates = Jinja2Templates(directory="templates")
origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False, default=str)


async def save_data_to_json():
    collection = db["channels_collection"]
    documents = collection.find()
    data = [doc for doc in documents]
    output_file = "channels.json"
    save_to_json(data, output_file)


@app.get('/meter/')
async def get_documents():
    await save_data_to_json()
    return await get_all_documents()


@app.get('/meter/{_id}')
async def get_current_meter(_id: str):
    await save_data_to_json()
    return await get_document_by_id(_id)


@app.post('/meter/')
async def meter_post(data: Meter):
    await save_data_to_json()
    return await meter_add(data)


@app.delete('/meter/{_id}')
async def meter_delete(_id: str):
    await save_data_to_json()
    return await meter_remove(_id)


@app.put('/meter/{_id}')
async def meter_put(_id: str, meter_name: str = None, meter_serial: str = None, channel_name: str = None,
                    physical_address: int = None, protocol_name: str = None, ki: int = None,
                    ku: int = None, active: bool = None):
    await save_data_to_json()
    return await meter_update(_id, meter_name, meter_serial, channel_name,
                              physical_address, protocol_name, ki, ku, active)


@app.post('/channel/')
async def channel_post(data: Channel):
    await save_data_to_json()
    return await channel_add(data)


@app.get('/channel/{_id}')
async def get_current_channel(_id: str):
    await save_data_to_json()
    return await get_channel_by_id(_id)


@app.get('/channel/')
async def get_channels():
    # await save_data_to_json()
    return await get_all_channels()


@app.delete('/channel/{_id}')
async def channel_delete(_id: str):
    await save_data_to_json()
    return await channel_remove(_id)


@app.put('/channel/{_id}')
async def channel_put(_id: str, name: str = None, type: str = None, ip: str = None,
                      port: str = None,
                      serial_port: str = None, baud_rate: str = None,
                      data_bits: str = None, parity: str = None, stop_bits: str = None, active: bool = None):
    await save_data_to_json()
    return await channel_update(_id, name, type, ip,
                                port, serial_port, baud_rate,
                                data_bits, parity, stop_bits, active)


@app.post('/group/')
async def group_post(data: Group):
    await save_data_to_json()
    return await group_add(data)


@app.get('/group/')
async def get_groups():
    await save_data_to_json()
    return await get_all_groups()


@app.get('/group/{_id}')
async def get_current_group(_id: str):
    await save_data_to_json()
    return await get_group_by_id(_id)


@app.put('/group/{_id}')
async def group_put(_id: str, group_name: str):
    await save_data_to_json()
    return await group_update(_id, group_name)


@app.delete('/group/{_id}')
async def group_delete(_id: str):
    await save_data_to_json()
    return await group_remove(_id)


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("channels.html", {"request": request})


@app.get("/meters", response_class=HTMLResponse)
async def read_channels(request: Request):
    return templates.TemplateResponse("meters.html", {"request": request})


@app.get("/groups", response_class=HTMLResponse)
async def read_channels(request: Request):
    return templates.TemplateResponse("groups.html", {"request": request})


@app.get("/download_group")
async def download_excel(filename: str):
    file_path = os.path.join("Excel", filename)

    if os.path.exists(file_path):
        response = FileResponse(file_path,
                                media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response.headers["Content-Disposition"] = f"attachment; filename={filename}"
        return response
    else:
        return "Excel file not found", status.HTTP_404_NOT_FOUND


@app.post("/upload_group")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join("Excel", "group.xlsx")

    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return {"filename": "group.xlsx"}


@app.post("/import_group")
def import_data():
    group_excel()
    return {"message": "Data imported successfully"}


@app.get("/download_channel")
async def download_excel(filename: str):
    file_path = os.path.join("Excel", filename)

    if os.path.exists(file_path):
        response = FileResponse(file_path,
                                media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response.headers["Content-Disposition"] = f"attachment; filename={filename}"
        return response
    else:
        return "Excel file not found", status.HTTP_404_NOT_FOUND


@app.post("/upload_channel")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join("Excel", "channel.xlsx")

    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return {"filename": "channel.xlsx"}


@app.post("/import_channel")
def import_data():
    channel_excel()
    return {"message": "Data imported successfully"}


@app.get("/download_meter")
async def download_excel(filename: str):
    file_path = os.path.join("Excel", filename)

    if os.path.exists(file_path):
        response = FileResponse(file_path,
                                media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response.headers["Content-Disposition"] = f"attachment; filename={filename}"
        return response
    else:
        return "Excel file not found", status.HTTP_404_NOT_FOUND


@app.post("/upload_meter")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join("Excel", "meter.xlsx")
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return {"filename": "meter.xlsx"}


@app.post("/import_meter")
def import_data():
    meter_excel()
    return {"message": "Data imported successfully"}


@app.get("/get_groups")
async def get_groups():
    groups = groups_collection.find({})
    return [{"group_name": group["group_name"], "vm_id": group.get("vm_id", [])} for group in groups]


@app.get("/get_meters")
async def get_meters():
    meters = meters_collection.find({})

    return [{"meter_name": meter["meter_name"], "protocol_name": meter["protocol_name"], "vm_id": meter["vm_id"],
             "meter_serial": meter["meter_serial"], "physical_address": meter["physical_address"],
             "channel_name": meter["channel_name"], "ki": meter["ki"], "ku": meter["ku"], "active": meter["active"],
             "group_name": meter.get("group_name", [])} for meter in meters]


@app.get("/get_channels")
async def get_channels():
    channels = channels_collection.find({})

    modified_channels = []
    for channel in channels:
        if channel["type"] == "TCP":
            channel_info = {"name": channel["name"], "type": channel["type"],"ip": channel["ip"], "port": channel["port"], "active": channel["active"]}
        elif channel["type"] == "COM":
            channel_info = {"name": channel["name"], "type": channel["type"], "serial_port": channel["serial_port"], "baud_rate": channel["baud_rate"], "stop_bits": channel["stop_bits"], "data_bits": channel["data_bits"], "active": channel["active"]}
        modified_channels.append(channel_info)

    return modified_channels