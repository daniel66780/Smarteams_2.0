<template>
    <!-- <Menu/> -->
    <div style="left: 40%;">
        <Register id="reg"/>
    </div>
    <!-- <router-link to="/Profile"> MI PERFIL </router-link>
    <RouterView/> -->
</template>

<script>
import Register from '@/components/register-page/Register.vue';
import Menu from '@/components/shared/menu.vue';

export default{
    name: 'RegisterPage',
    components: {
    Register,
    Menu,
    }
}
</script>

<style scoped>
</style>