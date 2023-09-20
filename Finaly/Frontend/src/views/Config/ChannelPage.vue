<template>
  <div class="content">
    <v-container>
      <h1>{{ this.$route.params.id }}</h1>
      <HeaderChannels/>
    </v-container>
  </div>
</template>

<script>
import HeaderChannels from "@/components/config/HeaderChannels";

export default {
  name: "ChannelPage",

  components: {
    HeaderChannels
  }
}
</script>

<style scoped>

</style>