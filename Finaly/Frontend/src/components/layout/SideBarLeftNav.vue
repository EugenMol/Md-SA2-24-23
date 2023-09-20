<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div app>
    <v-navigation-drawer app permanent width="fit-content">
      <v-list-item active-class="text--primary home" flat="true" background="white" link :to="{name: 'home'}">
        <v-list-item-content>
          <v-list-item-title class="text-h6">
            Конус
          </v-list-item-title>
          <v-list-item-subtitle>
            ООО "Автоматизация-2000"
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list nav>
        <!--       Меню мониторинга-->
        <v-list-group
            :value="false"
            prepend-icon="mdi-view-dashboard"
        >
          <template v-slot:activator>
            <v-list-item-title>Мониторинг</v-list-item-title>
          </template>

          <v-list-item
              v-for="([title, url], i) in monitoring"
              :key="i"
              :to="url"
              link
          >
            <v-list-item-title v-text="title"></v-list-item-title>
          </v-list-item>
        </v-list-group>


        <!--        Меню конфигурации-->
        <v-list-group
            :value="false"
            prepend-icon="mdi-image"
        >
          <template v-slot:activator>
            <v-list-item-title>Конфигурация</v-list-item-title>
          </template>

          <v-list-item
              v-for="([title, url], i) in configurations"
              :key="i"
              :to="url"
              link
          >
            <v-list-item-title v-text="title"></v-list-item-title>
          </v-list-item>
        </v-list-group>

        <v-list-item
            :to="{name: 'charts'}">
          <v-list-item-icon>
            <v-icon>mdi-chart-bar</v-icon>
          </v-list-item-icon>

          <v-list-item-title>Графики</v-list-item-title>
        </v-list-item>

        <v-list-item
            :to="{name: 'administration'}">
          <v-list-item-icon>
            <v-icon>mdi-help-box</v-icon>
          </v-list-item-icon>

          <v-list-item-title>Админка</v-list-item-title>
        </v-list-item>


      </v-list>
    </v-navigation-drawer>
  </div>
</template>

<script>
export default {
  name: "SideBarLeftNav",
  data() {
    return {
      items: [
        {title: 'Monitoring', icon: 'mdi-view-dashboard', url: {name: 'monitoring'}},
        {title: 'Configuration', icon: 'mdi-image', url: {name: 'configuration'}},
        {title: 'Administration', icon: 'mdi-help-box', url: {name: 'administration'}},
      ],
      configurations: [
        ['Каналы связи', {name: 'channels_conf'}],
        ['Приборы учета', {name: 'meters_conf'}],
        ['Группы опроса', {name: 'groups_conf'}],
        ['Объекты учета', {name: 'object_conf'}],

      ],
      monitoring: [
        ['Суточные отчеты', {name: 'monitorDate'}],
        ['Опросить', {name: 'queryForm'}],
      ],
    }
  }

}
</script>

<style>
.v-list-item__title {
  font-size: 0.8rem;
}

.v-application--is-ltr .v-list-item__icon:first-child {
  margin-right: 5px;
}

.v-application--is-ltr .v-list-item__icon:last-of-type:not(:only-child) {
  margin-left: 5px;
  width: fit-content;
}

.v-data-table--dense > .v-data-table__wrapper > table > thead > tr > th, .v-data-table--dense > .v-data-table__wrapper > table > tfoot > tr > th {
  height: 32px;
  width: min-content;
}

span {
  font-size: 11px;
  height: fit-content;

}

span.v-chip.v-size--default {
  height: fit-content;
}

.v-list-item--link::before {
  background-color: white;
}

/*/deep/ .v-chip.v-size--default {*/
/*  height: fit-content;*/
/*}*/

</style>