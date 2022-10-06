<template>
    <div >
        <h1 class="title">{{title1}}</h1>
    </div>
</template>

<script>
export default {
    props:['title'],
    name: 'pageTitle',
    data(){
      return{
        title1: this.title
      }
    },
}
</script>

<style scoped>
.title{
    background-color: #ffffff;
    color: #000000;
    text-align: left;
    padding: 0px 10px;
    font-size: 40px;
    font-weight: 800;
    font-family: Helvetica;
    /* border-radius: 18px; */
    /* right:200px; */
    height: 60px;
    /* width: 700px; */
    /* bottom: 50px */
}
</style>