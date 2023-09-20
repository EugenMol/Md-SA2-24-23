<template>
  <div class="wrapper">
    <div class="wrapper-content">
      <v-container>

        <!--      Форма создания новой группы-->
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
              New group
            </v-btn>
          </template>

          <v-card>
            <v-card-title class="text-h5 grey lighten-2">
              Создание группы опроса
            </v-card-title>

            <v-card-text>
              <v-form
                  ref="form"
                  lazy-validation
              >
                <v-text-field
                    v-model="group.group_name"
                    label="Название группы опроса"
                ></v-text-field>
              </v-form>
            </v-card-text>

            <v-divider></v-divider>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                  color="primary"
                  @click="Save(group)"
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
        <v-data-table
            :headers="headers"
            :items="GROUPS"
            class="elevation-1"
            :items-per-page="-1"
            hide-default-footer
            dense
        >

          <template v-slot:item.group_name="{ item }">
            <p style="cursor: pointer; " @click="editItem(item)">
              {{ item.group_name }}
            </p>
          </template>

          <!--Поле списка счетчикво в группе-->
          <template v-slot:item.meters="{ item }">
            <v-chip
                dense
                close
                class="ma-lg-2"
                @click:close="DeleteItem(meter, item)"
                v-for="(meter, index)  in item.meters"
                :key="index"
            >
              {{ meter.meter_name }}
            </v-chip>
          </template>
        </v-data-table>


        <!--      Форма редактиования групп опроса-->
        <v-dialog
            v-model="dialogEdit"
            max-width="500px"
        >
          <v-card>
            <v-card-title class="text-h5 grey lighten-2">
              Редактирование группы опроса
            </v-card-title>
            <v-card-text>
              <v-form
                  ref="form"
                  lazy-validation
              >
                <v-text-field
                    v-model="group.group_name"
                    label="Название группы опроса"
                ></v-text-field>

                <v-select v-model="selectedVMID" :items="METERS" item-text="meter_name" item-value="vm_id"
                          label="Выбор прибора учета...">
                </v-select>

                <label>Список счетчиков в группе</label>
                <v-divider></v-divider>
                <p v-for="meter in group.meters_list" :key="meter.vm_id">{{ meter.meter_name }}</p>
                <!--                    <v-select-->
                <!--                        v-model="type"-->
                <!--                        :items="type_of_channel"-->
                <!--                        label="Тип"-->
                <!--                    ></v-select>-->
              </v-form>
            </v-card-text>

            <v-card-actions>
              <v-btn @click="Submit(selectedVMID)">Submit</v-btn>
              <v-btn @click="dialogEdit = false">Close</v-btn>
            </v-card-actions>

          </v-card>
        </v-dialog>
      </v-container>
    </div>
  </div>


</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "GroupsPage",
  data() {
    return {
      dialog: false,
      dialogEdit: false,
      // addMeterToGroup: {vmid: '', group_id: ''},
      selectedVMID: '',
      group: {group_name: '', meters_list: '', group_id: ''},
      headers: [
        {text: 'ID Группы', value: 'group_id'},
        {text: 'Название группы', value: 'group_name'},
        {text: 'Список счетчиков в группе', value: 'meters'},

      ],
    }
  },

  methods:
      {
        ...mapActions([
          'GET_GROUPS_FROM_API',
          'POST_ADD_GROUP',
          'INCLUDE_METER_IN_GROUP',
          'EXCLUDE_METER'
        ]),

        DeleteItem(item, group) {
          const meter = {

            'vm_id': item.vm_id,
            'group_id': group.group_id
          }
          this.EXCLUDE_METER(meter)
          console.log(meter)
        },

        Save(group) {
          console.log(this.group)
          this.POST_ADD_GROUP(group)
          return this.dialog = false
        },
        editItem(item) {
          this.dialogEdit = true
          this.group.group_name = item.group_name
          this.group.meters_list = item.meters
          this.group.group_id = item.group_id

          console.log(item)
        },
        Submit(item) {
          let addMeterToGroup = {
            idx: this.GROUPS.map(g_id => g_id.group_id).indexOf(this.group.group_id),
            vm_id: item,
            group_id: this.group.group_id,
            meter: this.METERS.find(meter => meter.vm_id === item),
          }
          this.INCLUDE_METER_IN_GROUP(addMeterToGroup)
          console.log(addMeterToGroup)
          // this.dialogEdit = false
        },
      },

  computed: {
    ...mapGetters(
        [
          'GROUPS',
          'METERS',
        ],
    ),
  },
  mounted() {
    this.GET_GROUPS_FROM_API();
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