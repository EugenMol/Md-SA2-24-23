<template>
  <div>
    <v-container>
      <h1>MetersConfPage</h1>
      <ConfigMeters/>
    </v-container>
  </div>
</template>

<script>

import ConfigMeters from "@/components/config/ConfigMeters";

export default {
  name: "MetersConfPage",
  components: {
    ConfigMeters,
  }
}
</script>

<style scoped>

</style>