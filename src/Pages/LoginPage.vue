<template>
    <!-- <Menu/> -->
    <div style="left: 40%">
        <Login/>
    </div>

</template>

<script>
import Login from '@/components/login-page/Login.vue';
import Menu from '@/components/shared/menu.vue';

export default{
    name: 'RegisterPage',
    components: {
    Login,
    Menu,
    }
}
</script>

<style scoped>
</style>