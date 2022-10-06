<template>
    <div style="text-align: left; height: 520px; width: 520px; color: #FF5758;">

        <h1 style="font-size: 45px; font-weight: 800; color: #000000"> Añada una tarea </h1><br/>

        <p> Nombre de la tarea </p>
        <input type="text" v-model="taskname" class="field"><br/>

        <p> Integrante responsable: </p>
        <select id="user-select" v-model="taskuser" class="form">
            <option value="0"> Angelica Portocarrero </option>
            <option value="1"> John Smith </option>
            <option value="2"> Maria Quintero </option>
            <option value="3"> Mateo Colinas </option>
       </select><br/>

       <p>Fecha límite</p>
            <label for="day" class="label"> Día </label>
        <select id="day" v-model="day" class="form">
            <option value="0">01</option>
            <option value="1">02</option>
            <option value="2">03</option>
            <option value="3">04</option>
            <option value="4">05</option>
            <option value="5">06</option>
            <option value="6">07</option>
            <option value="7">08</option>
            <option value="8">09</option>
            <option value="9">10</option>
            <option value="10">11</option>
            <option value="11">12</option>
            <option value="12">13</option>
            <option value="13">14</option>
            <option value="14">15</option>
            <option value="15">16</option>
            <option value="16">17</option>
            <option value="17">18</option>
            <option value="18">19</option>
            <option value="19">20</option>
            <option value="20">21</option>
            <option value="21">22</option>
            <option value="22">23</option>
            <option value="23">24</option>
            <option value="24">25</option>
            <option value="25">26</option>
            <option value="26">27</option>
            <option value="27">28</option>
            <option value="28">29</option>
            <option value="29">30</option>
            <option value="30">31</option>
       </select>
       <label for="month" class="label"> Mes </label>
       <select id="month" v-model="month" class="form">
            <option value="0"> Enero</option>
            <option value="1">Febrero</option>
            <option value="2">Marzo</option>
            <option value="3">Abril</option>
            <option value="4">Mayo</option>
            <option value="5">Junio</option>
            <option value="6">Julio</option>
            <option value="7">Agosto</option>
            <option value="8">Septiembre</option>
            <option value="9">Octubre</option>
            <option value="10">Noviembre</option>
            <option value="11">Diciembre</option>
       </select>
       <label for="year" class="label"> Año </label>
       <select id="year" v-model="year" class="form">
            <option value="0">2022</option>
            <option value="1">2023</option>
            <option value="2">2024</option>
            <option value="3">2025</option>
       </select>

        <button @click="createTask()" class="btn"> Añadir tarea </button>
<!-- lo ideal seria que esto fuera un formulario que depsues insertara los datos del usuario en una tabla que seria la base de datos de los usuarios-->
    </div>
</template>

<script>
export default {
    name: 'AddTask',
    data(){
      return{
          taskname:"",
          taskuser:"",
          day: "",
          month: "",
          year: ""    
      }
    },
    methods:{
        createUser(){
            console.log("TAREA AÑADIDA")
        }
    }
}
</script>

<style scoped>
p{
    font-weight: 800;
    color: #FF5758;
    font-size: 20px
}
label{
    font-weight: 800;
    color: #FF5758;
    font-size: 20px
}
#user-select{
    width:200px;
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
.form{
  width: 150px;
  background-color: #EBE9E9;
  color: #5c5c5c;
  padding: 10px 5px;
  margin: 10px 0;
  border: none;
  border-radius: 24px;
  cursor: pointer;
  width: 80px;
}
#month{width: 100px;}
</style>