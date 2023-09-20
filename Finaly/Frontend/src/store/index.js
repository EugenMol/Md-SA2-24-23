import Vue from 'vue'
import Vuex from 'vuex'
import channels from '@/store/modules/config.channels.js'
import meters from '@/store/modules/config.meters.js'
import data from '@/store/modules/data.parametr'
import dataset from '@/store/modules/data_dash_1/data.dash1'
import groups from '@/store/modules/config.groups'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    channels,
    meters,
    groups,
    data,
    dataset
  }
})
