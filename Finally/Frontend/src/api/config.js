import axios from '@/api/axios';
import {markRaw} from "vue";


const get_channels =  (state, date) =>  axios.get(`/channel`)
const add_channel = (new_channel) => axios.post('/channel', new_channel);

const save_config = (state, date) => axios.get(`/save_config`);
const reload = (state, date) => axios.get(`/restart`);

const get_meters = (state, date) =>  axios.get(`/meter`)
const add_meter = (new_meter) => axios.post(`/meter`, new_meter);
const update_meter = (meter) => axios.post(`/update_meter`, meter);


const exclude_meter = (meter) => axios.post(`/exclude_meter`, meter);

// Работа с группами
const get_groups = () => axios.get(`/group`)
const add_group = (new_group) => axios.post(`/group`, new_group);
const include_meter = (adding_meter) => axios.post(`/include_meter`, adding_meter);

const get_all_config = async () => {
    const [channels, meters, groups] = await Promise.all([get_channels(), get_meters(), get_groups()])
    return {
        channels, meters, groups
    }
}


export default {
    get_all_config,
    get_channels,
    add_channel,
    get_meters,
    add_meter,update_meter,
    save_config,
    reload,
    exclude_meter,
    get_groups, add_group, include_meter

};
