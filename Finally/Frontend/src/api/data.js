import axios from '@/api/axios';


const get_data = (cmd, vm_id, from, to) => axios.get(`/getdata?cmd=${cmd}&vm_id=${vm_id}&from=${from}&to=${to}`);
const getmin_30 = (vm_id, from, to, energy) => axios.get(`/getmin30?vm_id=${vm_id}&from=${from}&to=${to}&energy=${energy}`);
const create_cmd = (query) => axios.post(`/create_cmd`, query);


const get_data_to_dash_1 = (vm_id, energy, date) => axios.get(`/test2?vm_id=${vm_id}&energy=${energy}&date=${date}`);



const send_cmd = (query) => axios.post(`/test2?vm_id=${vm_id}&energy=${energy}&date=${date}`);



export default {
  get_data, getmin_30, get_data_to_dash_1, send_cmd, create_cmd


};