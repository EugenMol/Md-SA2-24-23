<template>
  <div>
    <h1>Channels header</h1>
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
          New channel
        </v-btn>
      </template>


      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          Редактирование канала связи
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

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
              color="primary"
              @click="Save(name, ip, port, type)"
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
    <v-btn @click="SaveConfig"
    >
      Save
    </v-btn>

    <v-btn @click="Reload"
    >
      Reload
    </v-btn>

  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "HeaderChannels",

  data() {
    return {
      dialog: false,
      type_of_channel: ["TCP", "COM"],
      name: "",
      ip: "",
      port: "",
      type: ""

    }
  },
  methods:
      {
        ...mapActions([
          'ADD_CHANNEL',
          'SAVE_CONFIG',
          'RELOAD'
        ]),

        Save(name, ip, port, type) {
          let new_channel = {
            name: name,
            ip: ip,
            port: parseInt(port),
            type: type
          }
          console.log(new_channel);
          this.ADD_CHANNEL(new_channel)
          return this.dialog = false

        },

        SaveConfig() {
          console.log("Save config")
          this.SAVE_CONFIG()
        },
        Reload() {
          console.log("Reload config")
          this.RELOAD()
        }

      },

  computed: {
    ...mapGetters(
        [
          'NEW_CHANNEL',

        ],
    ),
  },

}
</script>

<style scoped>

</style>