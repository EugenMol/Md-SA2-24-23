<template>
  <div class="content">
    <v-container>
      <h1>DataPage</h1>
      <v-sheet>
        <v-row>
          <!--        <v-row align="stretch">-->
          <v-col
              class="d-flex"
              cols="12"
              sm="2"
          >
            <v-text-field
                dense
                outlined
                required
                :value="dateRangeText"
                label="Дата"
                @click="dataDialog=true"
            />
          </v-col>

          <v-col
              class="d-flex"
              cols="12"
              sm="3"
          >
            <v-select
                :items="GROUPS"
                item-text="group_name"
                item-value="group_id"
                dense
                outlined
                v-model="query.vm_id"
                label="Группа опроса"
            />
            <!--         -->
          </v-col>

          <v-col
              class="d-flex"
              cols="12"
              sm="5"
          >
            <v-select
                dense
                :items="cmds"
                item-text="title"
                item-value="name"
                v-model="query.cmd"
                outlined
                required
                label="Параметр"
            />
          </v-col>

          <v-col
              class="d-flex"
              cols="12"
              sm="2"
          >
            <div class="btn">
              <v-btn outlined @click="Show(query)">Показать</v-btn>
            </div>
          </v-col>
        </v-row>
        <v-row class="checkbox-ktr">
          <v-checkbox
              v-model="checkbox"
              label="Без учета КТР"
          ></v-checkbox>
        </v-row>
      </v-sheet>


      <v-dialog v-model="dataDialog"
                width="300"
      >
        <v-date-picker
            locale="Ru-ru"
            v-model="pickers"
            @keydown.enter="dataDialog=false"
        ></v-date-picker>
      </v-dialog>

      <v-card>
        <label>Показания на начало суток в период {{ query.from }}</label>
        <v-data-table
            :headers="headers"
            :items="QUERY.result"
            class="elevation-1"
            :items-per-page="-1"
            hide-default-footer
            dense
        >

          <template v-if="checkbox" v-slot:item.data[0].ep.t0="{item}">
            {{ Object.keys(item?.data[0].ep).length === 0 ? 'Н/Д' : (item?.data[0].ep.t0 / (item.ki * item.ku)).toFixed(3) }}
          </template>
          <template v-else v-slot:item.data[0].ep.t0="{item}">
             {{ Object.keys(item?.data[0].ep).length === 0 ? 'Н/Д' : (item?.data[0].ep.t0).toFixed(3) }}
          </template>


          <template v-if="checkbox" v-slot:item.data[0].em.t0="{item}">
            {{ Object.keys(item?.data[0].em).length === 0 ? 'Н/Д' : (item?.data[0].em.t0 / (item.ki * item.ku)).toFixed(3) }}
          </template>
          <template  v-slot:item.data[0].em.t0="{item}">
             {{ Object.keys(item?.data[0].em).length === 0 ? 'Н/Д' : (item?.data[0].em.t0).toFixed(3) }}
          </template>

          <template v-if="checkbox" v-slot:item.data[0].rp.t0="{item}">
            {{ Object.keys(item?.data[0].rp).length === 0 ? 'Н/Д' : (item?.data[0].rp.t0 / (item.ki * item.ku)).toFixed(3) }}
          </template>
          <template v-else v-slot:item.data[0].rp.t0="{item}">
            {{ Object.keys(item?.data[0].rp).length === 0 ? 'Н/Д' : (item?.data[0].rp.t0).toFixed(3) }}
          </template>

          <template v-if="checkbox" v-slot:item.data[0].rm.t0="{item}">
            {{ Object.keys(item?.data[0].rm).length === 0 ? 'Н/Д' : (item?.data[0].rm.t0 / (item.ki * item.ku)).toFixed(3) }}
          </template>
          <template v-else v-slot:item.data[0].rm.t0="{item}">
            {{ Object.keys(item?.data[0].rm).length === 0 ? 'Н/Д' : (item?.data[0].rm.t0).toFixed(3) }}
          </template>

          <template v-slot:item.meter_serial="{item}">
            {{ METERS.find(qqq => qqq.vm_id == item.vm_id).meter_serial }}
          </template>

        </v-data-table>
      </v-card>

    </v-container>


    <!--    Отчет по 30 минутным срезам  -->
    <v-container>
      <h1>30 min</h1>
      <v-row>
        <v-col
            class="d-flex"
            cols="12"
            sm="12"
        >
          <div class="btn">
            <v-btn outlined @click="Show_30min(query)">Показать</v-btn>
          </div>
        </v-col>

      </v-row>

      <!--      <v-card>-->
      <label>Срезы 30-минутной мощности {{ query.from }}</label>
<!--      <p>QUERY_MIN30.result.data {{ QUERY_MIN30.result }}</p>-->
      <!--        <p v-for="q in QUERY_MIN30.result" :key="q">{{ Object.keys(q.data[0].values) }}</p>-->

<!--      <p v-for="q in QUERY_MIN30.result" :key="q">{{ Object.values(q.data[0].values) }}</p>-->
<!--      <p>aksncasjdn = {{ values }}</p>-->
      <v-sheet
      class="v-sheet--offset mx-auto"
      elevation="12"
      max-width="calc(100% - 32px)"
    >
<!--      <v-sparkline-->
<!--        :value="values.num"-->
<!--        :labels="values.labels"-->
<!--        label-size="3"-->
<!--        line-width="2"-->
<!--        type="trend"-->
<!--      ></v-sparkline>-->
    </v-sheet>
      <!--      </v-sheet>-->
    </v-container>

    <v-data-table
        :headers="headers_for_min30"
        :items="QUERY_MIN30.result"
        class="elevation-1"
        :items-per-page="-1"
        hide-default-footer
        dense
    >
    </v-data-table>


  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "DataDayPage",
  data() {
    return {
      value: [],
      checkbox: false,
      dates: [],
      pickers: '',
      query: {
        vm_id: '',
        cmd: '',
        from: '',
        to: '',
      },
      cmds: [
        {name: "day", title: "Показания на начало суток"},
        {name: "incday", title: "Кол-во потребленной энергии за сутки"},
        {name: "allen", title: "Текущие показания"},
        {name: "month", title: "Показания на начало месяца"},
        {name: "incmonth", title: "Кол-во потребленной энергии за месяц"}
      ],

      dataDialog: false,
      headers: [
        {text: 'ID', value: 'id'},
        {text: 'Название ТУ', value: 'metername'},
        {text: 'Заводской номер ПУ', value: 'meter_serial'},
        {text: 'vm_id', value: 'vm_id'},
        {text: 'КТ', value: 'ki'},
        {text: 'КН', value: 'ku'},
        {text: 'Энергия активная принимаемая, кВт', value: 'data[0].ep.t0'},
        {text: 'Энергия активная отдаваемая, кВт', value: 'data[0].em.t0'},
        {text: 'Энергия реактивная принимаемая, кВар', value: 'data[0].rp.t0'},
        {text: 'Энергия реактивная отдаваемая, кВар', value: 'data[0].rm.t0'},
      ],

      headers_for_min30: [
        //   // {text: 'ID', value: `${Object.keys(this.QUERY_MIN30.data[0].values)}`},
        {text: 'Название ТУ', value: 'metername'},
        {text: '00:00 - 00:30', value: 'data[0].values.v1'},
        {text: '00:30 - 01:00', value: 'data[0].values.v2'},
        {text: '01:00 - 01:30', value: 'data[0].values.v3'},
        {text: '01:00 - 02:30', value: 'data[0].values.v4'},
        {text: 'V5', value: 'data[0].values.v5'},
        {text: 'V6', value: 'data[0].values.v6'},
        {text: 'V7', value: 'data[0].values.v7'},
        {text: 'V8', value: 'data[0].values.v8'},
        {text: 'V9', value: 'data[0].values.v9'},
        {text: 'V10', value: 'data[0].values.v10'},
        {text: 'V11', value: 'data[0].values.v11'},
        {text: 'V12', value: 'data[0].values.v12'},
        {text: 'V13', value: 'data[0].values.v13'},
        {text: 'V14', value: 'data[0].values.v14'},
        {text: 'V15', value: 'data[0].values.v15'},
        {text: 'V16', value: 'data[0].values.v16'},
        {text: 'V17', value: 'data[0].values.v17'},
        {text: 'V18', value: 'data[0].values.v18'},
        {text: 'V19', value: 'data[0].values.v19'},
        {text: 'V20', value: 'data[0].values.v20'},
        {text: 'V21', value: 'data[0].values.v21'},
        {text: 'V22', value: 'data[0].values.v22'},
        {text: 'V23', value: 'data[0].values.v23'},
        {text: 'V24', value: 'data[0].values.v24'},
      ]
    }
  },
  methods: {
    ...mapActions([
      'GET_DATA_FROM_QUERY', 'GET_GROUPS_FROM_API', 'GET_MIN_30_FROM_QUERY', 'GET_CREATE_CMD'
    ]),

    Show(query) {
      query.from = this.pickers
      query.to = this.pickers
      let idx = this.GROUPS.findIndex(item => item.group_id === query.vm_id)
      console.log(`idx = ${idx}`)
      query.vm_id = this.GROUPS[idx].meters.map(item => item.vm_id).join(',')
      console.log(`query.vm_id = ${query.vm_id}`)
      console.log(query.vm_id)
      // console.log(this.METERS.find(item => item.vm_id === 402).ki)

      this.GET_DATA_FROM_QUERY(query)
      // console.log(`getdata?vmid=${this.meterList}&cmd=${this.selectedCmd}&from=
      // ${this.dates[0]}&to=${this.dates[1]}`)
    },

    Show_30min(query) {
      query.from = this.pickers
      query.to = this.pickers
      let idx = this.GROUPS.findIndex(item => item.group_id === query.vm_id)
      console.log(`idx = ${idx}`)
      query.vm_id = this.GROUPS[idx].meters.map(item => item.vm_id).join(',')
      // query.vm_id = 68
      console.log(query)
      console.log(`30 min power`)
      this.GET_MIN_30_FROM_QUERY(query)
      // for (let q in this.QUERY_MIN30.result) {
      //   console.log(`Header = ${this.QUERY_MIN30.result}`)
      // }
    },


  },
  computed: {
    ...mapGetters(
        [
          'QUERY',
          'GROUPS',
          'QUERY_MIN30',
          'METERS'
        ]
    ),

    headers_test() {
      // return
    },

    values() {
      const object = this.QUERY_MIN30.result
      const val = {
        num:'',
        labels:''
      }

      // num = Object.values(this.QUERY_MIN30.result.data[0].values)
      for (let idx_num in object) {
        val.num = (Object.values(object[idx_num].data[0].values))
        // val.num.push(Object.values(object[idx_num].data[0].values))
        // val.labels.push(Object.keys(object[idx_num].data[0].values))
        val.labels = (Object.keys(object[idx_num].data[0].values))

      }
      return val
    },


    dateRangeText() {
      return this.pickers
      // return this.dates.join(' - ')
    },

  },
  created() {
    this.GET_GROUPS_FROM_API()
    const data = new Date();
    this.pickers = [data.getFullYear(), (`0${data.getMonth() + 1}`).slice(-2), data.getDate()].join('-');
  },
}
</script>

<style scoped>
/deep/ .v-btn:not(.v-btn--round).v-size--default {
  height: 40px;
}
/*.v-sheet {*/
/*  color: rgba(38, 172, 52, 0.87);*/
/*}*/

</style>