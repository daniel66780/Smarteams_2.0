<template>
  <!-- <div class="menu">
    <Menu/>
  </div> -->
  <div class="float-container">
    <div class="float-child" style="width: 52%; color:#FF5758;">
      <h1 style="font-weight: 800; font-size:50px"> ¡Bienvenid@ a Smarteams! </h1> <br/>
      <p style="font-weight: 500; font-size:20px; color:#000000;"> Una plataforma para crear equipos imparables. </p><br/>
      <router-link to="/Register" class="btn"> Registrarse </router-link><br/>
        <div style="height: 20px;"></div>
      <p style="font-style: italic; font-size:18px; color:#FF5758; margin: 10px;"> O, si ya tienes una cuenta... </p>
      <router-link to="/Login" class="btn"> Iniciar sesión </router-link>
      <RouterView />
    </div>
    <div class="float-child" id="img" style="align-items: center; background-color: #FF5758; border-radius: 30px; width: 48%;">
      <img src="@/assets/homepage-img.jpg" style="height: 400px; width:500px; border-radius: 30px;"/>
    </div>
  </div>


</template>

<script>
import Menu from '@/components/shared/menu.vue';

export default{
    name: 'HomePage',
    components: {
    Menu,
    }
}
</script>

<style scoped>

.btn{
  width: 200px;
  background-color: #FF5758;
  color: #ffffff;
  padding: 10px 20px;
  margin: 10px 0;
  border: none;
  border-radius: 24px;
  cursor: pointer;
  font-weight: 750;
  font-size: 18px;
  text-align:center;
}
.float-container {
    border: 3px solid rgb(255, 255, 255);
    padding: 20px;
    width: 1200px;
}
.float-child {
    float: left;
    padding: 30px;
    border: 2px solid #fff;
}  
#img{
  text-align: right;
}
</style>