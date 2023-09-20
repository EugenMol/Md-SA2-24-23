<template>
  <div>
    <h1>Comp meters</h1>
    <HeaderMeters/>
    <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
    ></v-text-field>
    <v-data-table
        :headers="headers"
        :items="METERS"
        class="elevation-1"
        :items-per-page="-1"
        :search="search"
        hide-default-footer
        dense
    >
      <template v-slot:item.meter_name="{ item }">
        <p style="cursor: pointer; " @click="editItem(item)">
          {{ item.meter_name }}
        </p>
      </template>

      <template v-slot:item.meter_id="{ item }">
          {{ METERS.findIndex(i => i._id == item._id) + 1 }}
      </template>

      <template v-slot:item.groups="{ item }">
        <v-chip
            dense
            close
            class="ma-lg-2"
            @click:close="DeleteItem(item1, item)"
            v-for="(item1, index)  in item.groups"
            :key="index"
        >
          {{ item1.group_name }}
        </v-chip>
      </template>
      <!--      <template v-slot:item.name="{ value }">-->
      <!--        <a :href="value">-->
      <!--          {{ value }}-->
      <!--        </a>-->
      <!--      </template>-->
    </v-data-table>

    <v-dialog
        v-model="dialogEdit"
        max-width="500px"
    >
      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          Редактирование канала связи
        </v-card-title>
        <v-card-text>
          <v-form ref="form" lazy-validation>
            <v-text-field v-model="meter.meter_name" label="Название канала связи"></v-text-field>
            <v-text-field v-model="meter.physical" label="Сетевой адрес"></v-text-field>
            <v-text-field v-model="meter.vm_id" label="VM_ID"></v-text-field>
            <v-text-field v-model="meter.meter_serial" label="Заводской номер"></v-text-field>
            <v-text-field v-model="meter.ki" label="Коэф. тока"></v-text-field>
            <v-text-field v-model="meter.ku" label="Коэф. напряжения"></v-text-field>
            <v-checkbox v-model="meter.active" :label="`Включен в опрос`"></v-checkbox>
            <v-select
                v-model="meter.channel_id"
                :items="this.CHANNELS"
                label="Канал связи"
                item-text="name"
                item-value="id">
            </v-select>
          </v-form>
        </v-card-text>

        <v-card-actions>
          <v-btn @click="Submit()">Submit</v-btn>
          <v-btn @click="dialogEdit = false">Close</v-btn>
        </v-card-actions>

      </v-card>
    </v-dialog>


  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";
import HeaderMeters from "@/components/config/HeaderMeters";

export default {
  name: "ConfigMeters",

  data() {
    return {
      search:'',
      dialogEdit: false,
      meter: {
        meter_name: '',
        protocol_name: '',
        meter_serial: '',
        meter_id: '',
        physical: '',
        vm_id: '',
        channel_id: '',
        channel_name: '',
        active: true,
      },
      headers: [
        {text: '#', value: 'meter_id'},
        {text: 'meter_name', value: 'meter_name'},
        {
          text: 'protocol_name',
          align: 'start',
          sortable: false,
          value: 'protocol_name',
        },
        {text: 'vm_id', value: 'vm_id'},
        {text: 'Заводской номер', value: 'meter_serial'},
        {text: 'physical_address', value: 'physical_address'},
        {text: 'channel_id', value: 'channel_name'},
        {text: 'ki', value: 'ki'},
        {text: 'ku', value: 'ku'},
        {text: 'Группа учета', value: 'groups'},

      ],
    }
  },

  methods:
      {
        ...mapActions([
          'GET_METERS_FROM_API',
          'EXCLUDE_METER',
          'UPDATE_METER'
        ]),
        DeleteItem(item, qqq) {
          // this.EXCLUDE_METER
          const meter = {

            'vm_id': qqq.vm_id,
            'group_id': item.group_id
          }
          this.EXCLUDE_METER(meter)
          console.log(meter)

          // console.log("Delete", item.group_id)
          // console.log("Delete", qqq.vm_id)
        },
        editItem(item) {
          console.log(item)
          this.dialogEdit = true
          this.meter.meter_name = item.meter_name
          this.meter.physical = item.physical_address
          this.meter.vm_id = item.vm_id
          this.meter.protocol_name = item.protocol_name
          this.meter.meter_serial = item.meter_serial
          this.meter.ki = item.ki
          this.meter.ku = item.ku
          this.meter.channel_id = item.channel_id
          this.meter.active = item.active
          this.meter.meter_id = item.meter_id
          console.log(this.meter)
        },
        Submit() {
          this.meter.ki = parseInt(this.meter.ki)
          this.meter.ku = parseInt(this.meter.ku)
          this.meter.physical = parseInt(this.meter.physical)
          this.meter.vm_id = parseInt(this.meter.vm_id)
          console.log(this.meter)
          this.UPDATE_METER(this.meter)
          this.dialogEdit = false
        }
      },

  computed: {
    ...mapGetters(
        [
          'METERS',
          'CHANNELS'
        ],
    ),
  },

  components: {
    HeaderMeters,

  },

  mounted() {
    this.GET_METERS_FROM_API();
  },
}
</script>

<style scoped>
p {
  margin: 0;
  color: #1633e0;
  text-decoration: underline;
}
</style>