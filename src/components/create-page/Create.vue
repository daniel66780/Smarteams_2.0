<template>
  <h1 style="font-size: 45px; font-weight: 800; color: #000000"> Crear un equipo </h1><br/>
  <div class="float-container">
    <div class="float-child">
        <p> Nombre del proyecto </p>
            <input type="text" id="pname" class="input" placeholder="Escribe aquí..." v-model="proyect_name">
        <p> Inserte los correos electrónicos de los usuarios </p>
            <textarea type="text" id="user-emails" class="input" placeholder="Separados por comas" v-model="proyect_users"> </textarea>
        <p style="font-style: italic"> Ó, Inserte una lista de usuarios (.csv / .xlsx)</p>
            <button id="insert" class="btn"> Insertar </button> <br/> 
            <!-- esto seria para adjuntar un csv donde esta la info de los usuarios y su perfil de pensamiento asignado -->
    </div>
    <div class="float-child">
            <p>Fecha límite</p>
            <label for="day" class="label"> Día </label>
        <select id="day" v-model="day" class="date-form">
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
       <select id="month" v-model="month" class="date-form">
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
       <select id="year" v-model="year" class="date-form">
            <option value="0">2022</option>
            <option value="1">2023</option>
            <option value="2">2024</option>
            <option value="3">2025</option>
       </select>
       <p>Añada una descripción</p>
        <textarea type="text" id="desc" class="input" placeholder="Escribe aquí..." v-model="proyect_desc"> </textarea> <br/>
       <button id="listo-btn" @click="createTeam()" class="btn">¡Listo!</button>
    </div>
  </div>
</template>

<script>
export default {
    name: 'Create',
    data(){
      return{
          proyect_name:"",
          proyect_users:"",
          day:"",
          month: "",
          year: "",
          proyect_desc:""
          }
    },
    methods:{
        createTeam(){
            console.log("EQUIPO CREADO")
        }
    }
}
</script>

<style scoped>
.float-container {
    border: 3px solid rgb(255, 255, 255);
    padding: 20px;
    width: 1200px;
}
.float-child {
    width: 50%;
    float: left;
    padding: 20px;
    border: none;
    background-color: #ffffff;
    color: #FF5758;
    text-align: left;
    font-size: 18px;
    padding: 1em;
    border-radius: 18px;
}  
.btn{
  width: 120px;
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
::placeholder{
  color: #a6a6a6;
  font-style: italic;
}
.label{
  color: #a6a6a6;
  font-style: italic;
}
.input{
  width: 300px;
  background-color: #EBE9E9;
  color: #5c5c5c;
  padding: 10px 17px;
  margin: 10px 0;
  border: none;
  border-radius: 24px;
  cursor: text;
  font-size: 18px;
}
#pname{
  height: 40px;
  width: 350px;
}
#desc{
  width: 350px;
  height: 150px;
  box-sizing: border-box;
  resize: none;
  font-family: helvetica;
  /* font-size: 14px; */
}
#user-emails{
  width: 350px;
  height: 100px;
  box-sizing: border-box;
  resize: none;
  font-family: helvetica;
  /* font-size: 14px; */
}
p{font-weight: 800;
font-size: 21px;
}
.date-form{
  width: 70px;
  background-color: #EBE9E9;
  color: #5c5c5c;
  padding: 5px 5px;
  margin: 10px 0;
  border: none;
  border-radius: 24px;
  cursor: pointer;
}
#month{width: 100px;}
#listo-btn{
  left: 230px;
}
</style>