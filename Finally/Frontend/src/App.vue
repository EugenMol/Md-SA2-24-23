<template>
  <v-app>
    <SideBarLeftNav/>
    <v-main>
      <v-container>
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>

import SideBarLeftNav from "@/components/layout/SideBarLeftNav";
import {mapActions, mapGetters} from "vuex";

export default {
  name: 'App',

  data: () => ({
    //
    base_url
  }),
  methods:
      {
        ...mapActions([
          'GET_CHANNELS_FROM_API', 'GET_METERS_FROM_API', 'GET_GROUPS_FROM_API'
        ])
      },
  computed: {
    ...mapGetters(
        [
          'METERS', 'GROUPS', 'CHANNELS'
        ],
    ),
  },
  mounted() {
    this.GET_CHANNELS_FROM_API();
    this.GET_GROUPS_FROM_API();
    this.GET_METERS_FROM_API();
  },
  components: {
    SideBarLeftNav,
  },
};
</script>
<style>
/*@import './assets/main.css';*/
@font-face {
  font-family: "Montserrat";
  font-weight: 300;
  font-style: normal;
  font-display: auto;
  unicode-range: U+000-5FF;
  src: local("Montserrat"), url("./assets/fonts/Montserrat/Montserrat-Medium.woff") format("woff");
}

.v-application {
  font-family: "Montserrat", sans-serif;
}

.v-main__wrap {
  background-color: #fafafa;
}

.col-sm-2 {
  justify-content: end;
}

.col-sm-12 {
  justify-content: end;
}
</style>