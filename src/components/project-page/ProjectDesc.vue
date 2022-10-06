<template>
    <div class="main-container">
      {{desc}}
    </div>
</template>

<script>
    export default {
        props: {
            "desc": String,
        },
        name: 'ProjectDesc',
    }
</script>

<style scoped>
    .main-container {
        min-height: 150px;
        width: 470px;
        background-color: #f1f1f1;
        color:#000;
        border-radius: 24px;
        padding: 20px;
        /* box-shadow: 10px 10px 10px #e3e3e3; */
    }
</style>