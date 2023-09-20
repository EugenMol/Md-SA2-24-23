<template>
  <div>
    <v-container>
      <div id="chart">
        <h1>Apex</h1>
        <!--        width="500"-->
        <apexchart
            type="heatmap"
            :options="options" :series="series" heigth="100">
        </apexchart>
        <h1>{{ daysInMonth }}</h1>
        <v-btn @click="ShowDayInMonth()">Нажать</v-btn>
        <!--        <apexchart type="heatmap" height="350" :options="chartOptions" :series="series"></apexchart>-->
      </div>
    </v-container>
  </div>

</template>

<script>
import moment from "moment";

export default {
  name: "Charts",
  // components: {
  //   apexchart: ApexCharts,
  // },
  data() {
    return {
      daysInMonth: '',
      options: {
        chart: {
          id: 'vuechart-example'
        },
        // xaxis: {
        //   categories: [
        //     "1",
        //     "2",
        //     "3",
        //     "4",
        //     "5",
        //     "6",
        //     "7",
        //     "8",
        //     "9",
        //     "10",
        //     "11",
        //     "12"
        //   ]
        // },
        title: {
          text: 'Полнота данных за месяц'
        },
        plotOptions: {
          heatmap: {
            shadeIntensity: 0.5,
            radius: 2,
            useFillColorAsStroke: false,
            colorScale: {
              ranges: [{
                from: 1,
                to: 47,
                name: 'Данные есть частично',
                color: '#FFB200'
              },
                {
                  from: 47,
                  to: 48,
                  name: 'Все данные есть',
                  color: '#00A100'
                },
                {
                  from: 0,
                  to: 1,
                  name: 'Данных нет',
                  color: '#FF0000'
                },
              ]
            }
          },
        },
      },

      series: [
        // {
        //   vmid: "Точка учета 1",
        //   data: [
        //     // {
        //     //   x: 'W1',
        //     //   y: 22
        //     // }, {
        //     //   x: 'W2',
        //     //   y: 29
        //     // }, {
        //     //   x: 'W3',
        //     //   y: 13
        //     // }, {
        //     //   x: 'W4',
        //     //   y: 13
        //     // }, {
        //     //   x: 'W5',
        //     //   y: 32
        //   ]
        // },
        // {
        //   vmid: "Точка учета 2",
        //   data: [{
        //     x: 'W1',
        //     y: 48
        //   }, {
        //     x: 'W2',
        //     y: 48
        //   }, {
        //     x: 'W3',
        //     y: 48
        //   }, {
        //     x: 'W4',
        //     y: 43
        //   }]
        // }
      ],

      // series: [{
      //   name: 'series-1',
      //   data: [55, 62, 89, 66, 98, 72, 101, 75, 94, 120, 117, 139]
      // }]


      // series: [{
      //   name: 'Metric1',
      //   data: generateData(18, {
      //     min: 0,
      //     max: 90
      //   })
      // },
      //   {
      //     name: 'Metric2',
      //     data: generateData(18, {
      //       min: 0,
      //       max: 90
      //     })
      //   },
      //   {
      //     name: 'Metric3',
      //     data: generateData(18, {
      //       min: 0,
      //       max: 90
      //     })
      //   },
      //   {
      //     name: 'Metric4',
      //     data: generateData(18, {
      //       min: 0,
      //       max: 90
      //     })
      //   },
      //   {
      //     name: 'Metric5',
      //     data: generateData(18, {
      //       min: 0,
      //       max: 90
      //     })
      //   },
      //   {
      //     name: 'Metric6',
      //     data: generateData(18, {
      //       min: 0,
      //       max: 90
      //     })
      //   },
      //   {
      //     name: 'Metric7',
      //     data: generateData(18, {
      //       min: 0,
      //       max: 90
      //     })
      //   },
      //   {
      //     name: 'Metric8',
      //     data: generateData(18, {
      //       min: 0,
      //       max: 90
      //     })
      //   },
      //   {
      //     name: 'Metric9',
      //     data: generateData(18, {
      //       min: 0,
      //       max: 90
      //     })
      //   }
      // ],
      // chartOptions: {
      //   chart: {
      //     height: 350,
      //     type: 'heatmap',
      //   },
      //   dataLabels: {
      //     enabled: false
      //   },
      //   colors: ["#008FFB"],
      //   title: {
      //     text: 'HeatMap Chart (Single color)'
      //   },
      // },
    }
  },
  methods: {
    ShowDayInMonth() {
      this.daysInMonth = moment('2023-05').daysInMonth()
      for (let step = 0; step < 10; step++) {
        this.series.push({name:`Num ${step}`, data:[]})
        for (let i = 1; i < this.daysInMonth; i++) {
          this.series[step].data.push({x: i, y: i + 30})
          console.log(i)
        }
      }
      console.log(this.series)
    },
  }
}
</script>

<style scoped>

</style>