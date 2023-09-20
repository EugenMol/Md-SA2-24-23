<template>
  <div class="content">
    <v-container>
    <p>ConfigurationPage</p>

    <HeaderChannels/>

    <ConfigChannels/>
</v-container>
  </div>
</template>

<script>
import ConfigChannels from "@/components/config/ConfigChannels";
import {mapActions, mapGetters} from "vuex";
import HeaderChannels from "@/components/config/HeaderChannels";

export default {
  name: "ConfigurationPage",
  data() {
    return {}
  },
  components: {
    ConfigChannels,
    HeaderChannels
  }
}
</script>

<style scoped>

</style>