<template>
  <div>
    <h1>Meters header</h1>
    <v-dialog
        v-model="dialog"
        width="500"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn
            color="red lighten-2"
            dark
            v-bind="attrs"
            v-on="on"
        >
          New meter
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          Создание прибора учета
        </v-card-title>

        <v-card-text>
          <v-form
              ref="form"
              lazy-validation
          >
            <v-text-field
                v-model="added_meter.meter_name"
                label="Название счетчика"

            ></v-text-field>
            <v-select
                :items="this.CHANNELS"
                item-text="name"
                item-value="id"
                v-model="added_meter.channel_id"
                label="Имя канала"
            ></v-select>

            <v-text-field
                v-model="added_meter.vm_id"
                label="VMID"
            ></v-text-field>

            <v-text-field
                v-model="added_meter.physical"
                label="Физический адрес устройства"
            ></v-text-field>

            <v-text-field
                v-model="added_meter.protocol_name"
                label="Тип счетчика"
            ></v-text-field>

            <v-text-field
                v-model="added_meter.ki"
                label="KI"
            ></v-text-field>

            <v-text-field
                v-model="added_meter.ku"
                label="KU"
            ></v-text-field>

            <v-checkbox
                v-model="added_meter.active"
                :label="`Включен в опрос: ${added_meter.active}`"
            ></v-checkbox>

            <!--            <v-select-->
            <!--                v-model="type"-->
            <!--                :items="type_of_channel"-->
            <!--                label="Тип"-->
            <!--            ></v-select>-->
          </v-form>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
              color="primary"
              @click="Save(added_meter)"
          >
            Save
          </v-btn>
          <v-btn
              color="primary"
              text
              @click="dialog = false"
          >
            Cancel
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "HeaderMeters",
  // props: {
  //   ki:  Number,
  // },
  data() {
    return {
      ki:0,
      dialog: false,
      added_meter: {
        meter_name: "",
        channel_id: "",
        vm_id: "",
        physical: "",
        protocol_name: "ss301",
        ki: 1,
        ku: 1,
        active: true,
      },
    }
  },
  methods:
      {
        ...mapActions([
          'ADD_METER',
        ]),

        Save(new_meter) {
          new_meter.vm_id    = parseInt(new_meter.vm_id)
          new_meter.physical = parseInt(new_meter.physical)
          new_meter.ki       = parseInt(new_meter.ki)
          new_meter.ku       = parseInt(new_meter.ku)
          new_meter.active = Number(new_meter.active)
          this.ADD_METER(new_meter)
          return this.dialog = false

        },
      },

  computed: {
    ...mapGetters(
        [
          'NEW_CHANNEL',
          'CHANNELS',
        ],
    ),
  },

}
</script>

<style scoped>

</style>