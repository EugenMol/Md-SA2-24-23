import Vue from 'vue'
import './plugins/axios'
import '@mdi/font/css/materialdesignicons.css'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import moment from 'moment';
import ApexCharts from 'apexcharts'

import '@/plugins/apexcharts'

Vue.config.productionTip = false

Vue.use(vuetify, {iconfont: 'mdi'})

new Vue({
  router,
  store,
  vuetify,
  moment,
  // ApexCharts,
  render: function (h) { return h(App) }
}).$mount('#app')
