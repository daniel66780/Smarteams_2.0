<template>
    <!-- <Menu/> -->
    <h1 style="font-size: 45px; font-weight: 800; color: #000000"> Mi perfil </h1><br/>
    <div class="float-container">
        <div class="float-child">
            <UserInfo  username="Angelica Portocarrero Quintero" useremail="angelica.portocarrero12+1@gmail.com"/>
            <div style="height:20px;"></div>
            <router-link to="/Create" id="create-btn"> + Crear un equipo </router-link>
            <RouterView />
            <div style="height:40px;"></div>
            <h2> Mis proyectos </h2>
            <!-- <UserProject projectName="Proyecto 1" projectDesc="Lorem ipsum dolor sit amet, consectetur adipiscing elit."/> -->
            <UserProject projectname="Proyecto 1"/>
            <UserProject projectname="Proyecto 2"/>
        </div>
        <div class="float-child" >
            <!-- <Desarrollador/> -->
            <!-- <Clarificador/> -->
            <!-- <Ideador/> -->
            <Implementador/>
            <div style="height:40px;"></div>
            <h2> Mis tareas asignadas </h2>
            <Task TaskName="Lorem Ipsum sit amet" deadline="dd-mm-yy"/><br/> 
            <Task TaskName="Lorem Ipsum sit amet" deadline="dd-mm-yy"/><br/> 
            <Task TaskName="Lorem Ipsum sit amet" deadline="dd-mm-yy"/><br/> 
        </div>
    </div>
</template>

<script>
import Menu from '@/components/shared/menu.vue';
import UserInfo from '@/components/profile-page/UserInfo.vue';
// import UserRole from '@/components/profile-page/UserRole.vue';
import Desarrollador from '@/components/profile-page/DesarrolladorRole.vue';
import Clarificador from '@/components/profile-page/ClarificadorRole.vue';
import Ideador  from '@/components/profile-page/IdeadorRole.vue';
import Implementador from '@/components/profile-page/ImplementadorRole.vue';

import UserProject from '@/components/profile-page/UserProject.vue';
import Task from '@/components/shared/Task.vue';

export default{
    name: 'ProfilePage',
    components: {
    Menu,
    UserInfo,
    // UserRole,
    Desarrollador,
    Clarificador,
    Ideador,
    Implementador,
    UserProject,
    Task
    },
}
</script>

<style scoped>
.float-container {
    /* border: 3px solid rgb(255, 255, 255); */
    border: none;
    padding: 20px;
    width: 1200px;
    min-height: 500px;
}
.float-child {
    width: 50%;
    float: left;
    padding: 20px;
    /* border:none; */
    background-color: #ffffff;
    color: #000000;
    font-size: 18px;
    padding: 1em;
    min-height: 500px;
}  
h2{
    font-weight: 750;
    font-size:30px;
}
#create-btn{
    width: 100px;
    background-color: #FF5758;
    color: #ffffff;
    padding: 15px 20px;
    margin: 10px 0;
    border: none;
    border-radius: 24px;
    cursor: pointer;
    font-size: 25px;
    font-weight: 800;
    top:20px;
    bottom:20px;
}
</style>