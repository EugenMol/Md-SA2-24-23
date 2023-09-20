<template>
  <div>
    <p>QueryPage</p>
    <v-card rounded="10">
      <v-card-title>Опросить ПУ</v-card-title>
      <v-card-text>

        <v-select dense outlined required v-show="groupCheckbox" label="Выбор группы учета" :items="this.GROUPS"
                  item-text="group_name" item-value="group_id" v-model="query.groups" chips multiple></v-select>
        <v-select dense outlined required v-show="!groupCheckbox" label="Выбор прибора учета" :items="this.METERS"
                  item-text="meter_name" item-value="vm_id" v-model="query.vm_id" chips multiple></v-select>
        <v-checkbox dense outlined required label="Опрос группы" v-model="groupCheckbox"></v-checkbox>
        <v-select dense outlined required label="Выбор параметра" :items="cmds" item-text="title" item-value="name"
                  v-model="query.commands" chips multiple></v-select>
        <v-text-field dense outlined required label="Выбор периода" :value="dateRangeText" @click="dataDialog=true"/>
        <v-btn @click="queryMeter(query)">Опросить</v-btn>


        <v-dialog v-model="dataDialog" width="300">
          <v-date-picker locale="Ru-ru" v-model="dates" range @keydown.enter="dataDialog=false"></v-date-picker>
        </v-dialog>

      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";
import moment from "moment";

export default {
  name: "QueryPage",
  data() {
    return {
      dates: [],
      groupCheckbox: false,
      query: {
        vm_id: [],
        groups: [],
        commands: [],
        from: '',
        to: '',
        ago: '',
        cnt: '',
      },
      dataDialog: false,

      cmds: [
        {name: "day", title: "Показания на начало суток"},
        {name: "incday", title: "Кол-во потребленной энергии за сутки"},
        {name: "allen", title: "Текущие показания"},
        {name: "month", title: "Показания на начало месяца"},
        {name: "incmonth", title: "Кол-во потребленной энергии за месяц"},
        {name: "min30", title: "Срезы 30-минутной мощности"}
      ],
    }
  },
  computed: {
    ...mapGetters(
        [
          'METERS',
          'CHANNELS',
          'GROUPS'
        ],
    ),

    dateRangeText() {
      return this.dates.join(' - ')
    },
  },
  methods: {
    ...mapActions([
      'GET_CREATE_CMD'
    ]),


    queryMeter(query) {
      query.from = this.dates[0]
      query.to = this.dates[1]
      query.commands = query.commands.join()
      query.vm_id = query.vm_id.join()
      query.groups = query.groups.join()
      console.log(`Send Meters Query's ${query}`)
      console.log(query)
      console.log(query.from.split('-'))
      let new_arr_from = query.from.split('-').map(item => parseInt(item))
      new_arr_from[1] -=1

      let new_arr_to = query.to.split('-').map(item => parseInt(item))
      new_arr_to[1] -=1
      console.log(moment(new_arr_from))
      // console.log(moment().diff(moment(new_arr_from), 'days'))
      query.ago = moment().diff(moment(new_arr_to), 'days')
      console.log(query.ago)
       console.log(moment(new_arr_to))
      query.cnt = moment(new_arr_to).diff(moment(new_arr_from), 'days') + 1
      console.log(query.cnt)
      this.GET_CREATE_CMD(query)

      query.vm_id = []
      query.groups = []
      query.commands = []
    }
  }
}
</script>

<style scoped>

</style>