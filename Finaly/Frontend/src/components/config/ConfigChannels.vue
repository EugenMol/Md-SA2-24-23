<template>
  <div>
    <v-data-table
        :headers="headers"
        :items="CHANNELS"
        class="elevation-1"
        :items-per-page="-1"
        hide-default-footer
        dense
    >

      <!-- , :activator="{ on, attrs }"-->
      <template v-slot:item.name="{ item }">
        <p style="cursor: pointer; " @click="editItem(item)">
          {{ item.name }}
        </p>
      </template>


    </v-data-table>
    <v-dialog
        v-model="dialog"
        max-width="500px"
    >
      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          Редактирование точки учета
        </v-card-title>
        <v-card-text>
          <v-form
              ref="form"
              lazy-validation
          >
            <v-text-field
                v-model="name"
                label="Название канала связи"
            ></v-text-field>

            <v-text-field
                v-model="ip"
                label="IP адрес"
            ></v-text-field>

            <v-text-field
                v-model="port"
                label="IP порт"

            ></v-text-field>

            <v-select
                v-model="type"
                :items="type_of_channel"
                label="Тип"
            ></v-select>
          </v-form>
        </v-card-text>

      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "ConfigChannels",
  data() {
    return {
      dialog: false,
      name: "",
      ip: "",
      port: "",
      type: "",
      type_of_channel: ["TCP", "COM"],
      headers: [
        {text: 'ID', value: 'id'},
        {
          text: 'Название канала',
          align: 'start',
          sortable: false,
          value: 'name',
        },
        {text: 'Тип', value: 'type'},
        {text: 'IP', value: 'ip'},
        {text: 'Port', value: 'port'},
        {text: 'serial_port', value: 'serial_port'},
        {text: 'baud_rate', value: 'baud_rate'},
        {text: 'stop_bits', value: 'stop_bits'},
        {text: 'data_bits', value: 'data_bits'},
        {text: 'active', value: 'active'},
      ],
    }
  },

  methods:
      {
        ...mapActions([
          'GET_CHANNELS_FROM_API',
        ]),

        editItem(item) {
          this.dialog = true
          this.name = item.name
          this.ip = item.ip
          this.port = item.port
          this.type = item.type
          console.log(item)
        }
      },

  computed: {
    ...mapGetters(
        [
          'CHANNELS',
        ],
    ),
  },

  mounted() {
    this.GET_CHANNELS_FROM_API();
  },
}
</script>

<style scoped>
p {
  margin: 0;
  color: #1633e0;
  text-decoration: underline;
  /* Смещаем подчёркивание на 20 пикселей вниз */
  /*text-underline-offset: 20px;*/
}
</style>