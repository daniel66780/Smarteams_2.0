<template>
    <!-- <Menu/> -->

    <!-- <nav style="background-color: #FF5758; color:#ffffff"> SMARTEAMS </nav>  -->
    <!-- navbar provisional ksjnfn -->

    <!-- <div style="clear: both;"></div> -->
    <Create id="create"/>
</template>

<script>
import Create from '@/components/create-page/Create.vue';
import Menu from '@/components/shared/menu.vue';

export default{
    name: 'CreatePage',
    components: {
    Create,
    Menu,
    }
}
</script>

<style scoped>

</style>