<template>
    <div style="text-align: center; height: 520px; width: 520px; color: #FF5758;">

        <h1 style="font-size: 45px; font-weight: 800; color: #000000"> Regístrate ahora </h1><br/>

        <p>Ingrese su nombre completo: </p>
        <input type="text" v-model="username" class="field"><br/>

        <p>Ingrese su correo electónico: </p>
        <input type="text" v-model="email" class="field"><br/>

        <p>Cree una contraseña: </p>
        <input type="password" v-model="password" class="field"><br/>

        <p>Vuelva a ingresar la contraseña: </p>
        <input type="password" v-model="password2" class="field"><br/>

        <p> Seleccione su perfil de pensamiento FourSight: </p>
        <select id="year" v-model="year" class="date-form">
            <option value="0">Ideador</option>
            <option value="1">Clarificador</option>
            <option value="2">Desarrollador</option>
            <option value="3">Implementador</option>
       </select><br/>
       <router-link to="/Login" @click="createUser()" class="btn" > Crear usuario </router-link>
        <RouterView />
<!-- lo ideal seria que esto fuera un formulario que depsues insertara los datos del usuario en una tabla que seria la base de datos de los usuarios-->
    </div>
</template>

<script>
export default {
    name: 'Register',
    data(){
      return{
          username:"",
          email:"",
          password: "",
          password2: ""     
      }
    },
    methods:{
        createUser(){
            console.log("NUEVO USUARIO REGISTRADO")
        }
    }
}
</script>

<style scoped>
/* .box{
    background-color: #ffffff;
    color: #FF5758;
    text-align: center;
    font-size: 16px;
    font-family: helvetica;
    padding: 0px 5px;
    border-radius: 18px;
    height: 450px;
    width: 350px;
    right: 700px;
    top: 100px
} */
p{
    font-weight: 800;
    color: #FF5758;
    font-size: 20px
}
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
  display: inline-block;
}
.field{
  width: 250px;
  background-color: #EBE9E9;
  color: #5c5c5c;
  padding: 10px 17px;
  margin: 10px 0;
  border: none;
  border-radius: 24px;
  cursor: text;
}
.date-form{
  width: 150px;
  background-color: #EBE9E9;
  color: #5c5c5c;
  padding: 10px 5px;
  margin: 10px 0;
  border: none;
  border-radius: 24px;
  cursor: pointer;
}
</style>