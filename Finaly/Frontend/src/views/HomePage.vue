<template>
  <v-container class="my-dashboard-1 grey lighten-5">
    <p>URL : {{ url }}</p>
    <div class="dash-1">
      <v-row justify="center">
        <v-col>
          <v-card class="pa-2 card_dash-1 rounded-xl" height="320px" min-width="350px">
            <v-card-title>{{ dash_item[0].title }}</v-card-title>
            <v-card-subtitle>{{ dash_item[0].subtitle }}</v-card-subtitle>

            <v-card-text class="report">
              <span>Утренний максимум: </span>
              <h1>{{ this.DATASET_1.result.time_index[0].maximum * 2 }}</h1>
            </v-card-text>
            <v-card-text class="report">
              <span>Вечерний максимум: </span>
              <h1>{{ this.DATASET_1.result.time_index[1].maximum * 2 }}</h1>
            </v-card-text>
            <v-card-text class="report">
              <span>Абсолютный максимум: </span>
              <h1>{{ this.DATASET_1.result.maximum_absolute * 2 }}</h1>
            </v-card-text>
          </v-card>
        </v-col>

        <v-col>
          <v-card class="pa-2 card_dash-1 rounded-xl" height="320px" min-width="350px">
            <v-card-title>{{ dash_item[1].title }}</v-card-title>
            <v-card-subtitle>{{ dash_item[1].subtitle }}</v-card-subtitle>
            <v-card-text class="report">
              <span>Расход за сутки</span>
              <h1>{{ this.DATASET_1.result.energy_day.value }}</h1>
            </v-card-text>

            <v-card-text class="report">
              <span>Расход в полупиковой зоне:</span>
              <h1>{{ this.DATASET_1.result.energy_half_peek.value }}</h1>
            </v-card-text>
            <v-card-text class="report">
              <span>Расход в пиковой зоне:</span>
              <h1>{{ this.DATASET_1.result.energy_peek.value }}</h1>
            </v-card-text>
            <v-card-text class="report">
              <span>Расход в ночной зоне:</span>
              <h1>{{ this.DATASET_1.result.energy_night.value }}</h1>
            </v-card-text>

          </v-card>
        </v-col>

        <v-col>
          <v-card class="pa-2 card_dash-1 rounded-xl" height="320px" min-width="350px">
            <v-card-title>{{ dash_item[2].title }}</v-card-title>
            <v-card-text>{{ dash_item[2].text }}</v-card-text>
            <v-card-text>
              <p></p>
            </v-card-text>
          </v-card>
        </v-col>

      </v-row>
      <v-row justify="center">
        <v-col cols="12">
          <v-card class="pa-2 card_dash-1 rounded-xl" height="fit-content">
            <v-sparkline
                :value="Object.values(this.DATASET_1.result.data)"
                :gradient="['#5ebcf7','#346cad']"
                :labels="Object.keys(this.DATASET_1.result.data)"
                label-size="3"
                line-width="4"
                padding="2"
                type="bar"
            ></v-sparkline>
          </v-card>

        </v-col>
        <h1>{{ this.currentTime }}</h1>
      </v-row>
    </div>
  </v-container>

</template>

<script>

import {mapActions, mapGetters} from "vuex";
import moment from "moment";

export default {
  name: 'Home',
  data() {
    return {
      url: process.env.VUE_APP_URL,
      currentTime: null,
      label_min30: [
        "00:00-00:30",
        "00:30-01:00",
        "01:00-01:30",
        "01:30-02:00",
        "02:00-02:30",
        "02:30-03:00",
        "03:00-03:30",
        "03:30-04:00",
        "04:00-04:30",
        "04:30-05:00",
        "05:00-05:30",
        "05:30-06:00",
        "06:00-06:30",
      ]
    }
  },
  methods: {
    ...mapActions([
      'GET_DATASET_1_FROM_API',
    ]),
  },
  computed: {
    ...mapGetters(
        [
          'DATASET_1',
        ]
    ),
    dash_item() {
      this.dataset = 16
      const dash = [
        {
          name: 'max1', title: 'Максимумы мощности, кВт ', subtitle: 'за предыдущие сутки', text:
              [
                {name: 'P_max_morn', title: 'зоны утреннего пика', value: 12},
                {name: 'P_max_evng', title: 'зоны вечернего пика', value: 12},
                {name: 'P_max_night', title: 'ночной зоны', value: 12},
              ]
        },
        {name: 'max2', title: 'Расход энергии, кВт*ч', subtitle: 'за предыдущие сутки'},
        {name: 'max3', title: 'max3'},
        {name: 'max4', title: 'max4'},
      ]
      return dash
    },


  },
  created() {
    let query_obj = {
      vm_id: 8,
      energy: 'ep',
      date: ''
    }
    this.currentTime = moment().subtract(1,'day').format('YYYY-MM-DD');
    query_obj.date = this.currentTime
    this.GET_DATASET_1_FROM_API(query_obj)
  },
}
</script>

<style scoped>
/*.my-dashboard-1 {*/
/*/ / background-color: aliceblue;*/
/*}*/

.dash-1 {
  height: 100vh;
  flex-wrap: wrap;

}

.report {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
}

span {
  font-size: 14px;
}
</style>
