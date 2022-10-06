<template>
    <!-- <Menu/> -->
    <!-- <router-link to="/Profile"> MI PERFIL </router-link>
    <RouterView /> -->
    <!-- <nav style="background-color: #FF5758; color:#ffffff"> SMARTEAMS </nav>  -->
    <!-- navbar provisional ksjnfn -->
    <Task/>
</template>

<script>
import Menu from '@/components/shared/menu.vue';
import Task from '@/components/task-page/CreateTask.vue';

export default{
    name: 'TaskPage',
    components: {
    Menu,
    Task
    }
}
</script>

<style scoped>

</style>