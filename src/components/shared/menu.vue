<template>
    <div class="container">
        <div class="rectangle">
            <h1 class="title">Smarteams</h1>
        </div>
        <div class="rectangle-left">
            <div>        
                <img class="img" src="https://img.freepik.com/vector-premium/icono-plano-usuario-anonimo-ilustracion-vector-larga-sombra_520826-1932.jpg"/>
            </div>
            <h1 class="user-name">John Smith</h1>
        </div> 
    </div>  
</template>

<script>
export default {
    name: 'Menu',
    data(){
    }
}
</script>

<style scoped>
/* h1{font-weight: 800;} */
.container{
    bottom: 0px;
    right: 50px;
}
.rectangle {
  height: 75px;
  width: 1515px;
  background-color: #FF5758;
  bottom: 290px;
  right: 100px;
  box-shadow: 120px 80px 40px 20px rgb(255, 255, 255)
}
.rectangle-left {
  height: 75px;
  width: 300px;
  background-color: #f93e3e;
  bottom: 365px;
  left: 1110px
}
.img {
  height: 50px;
  width: 50px;
  top: 15px;
  left: 10px;
  border-radius: 50%
}
.title{
    color: #ffffff;
    text-align: left;
    padding: 0px 10px;
    font-size: 40px;
    font-weight: 800;
    font-family: Helvetica;
    border-radius: 18px;
    height: 60px;
    width: 700px;
    top: 5px;
    left: 70px
}
.user-name{
    color: #ffffff;
    text-align: left;
    padding: 0px 10px;
    font-size: 20px;
    font-weight: 700;
    font-family: Helvetica;
    border-radius: 18px;
    height: 60px;
    width: 700px;
    bottom: 33px;
    left: 60px
    
}
.box{
    background-color: #ffffff;
    color: #FF5758;
    text-align: left;
    font-size: 16px;
    font-family: helvetica;
    padding: 1em;
    border-radius: 18px;
    height: 520px;
    width: 350px;
    right: 700px;
    top: 90px
}
</style>