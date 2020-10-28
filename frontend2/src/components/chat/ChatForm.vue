<template>
      <v-form
        ref="form"
        v-model="form"
        class="pa-4 pt-6"
    >
        <v-text-field
        v-model="title"
        filled
        label="Message Title"
        ></v-text-field>
        <v-textarea
        v-model="content"
        auto-grow
        filled
        color="primary"
        label="content"
        rows="5"
        ></v-textarea>

    </v-form>
</template>

<script>
export default {

}
</script>

<style>

</style>