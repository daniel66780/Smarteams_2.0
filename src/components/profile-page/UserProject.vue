<template>
    <div class="main-container">
        <div class="right-container" style="width: 25%; height: 100%;float:left; ">
            <img src="@/assets/project-img.png" style="height: 100px; width:100px">
        </div>
        <div class="left-container" style="width: 75%; height: 100%; float:right; ">
            <!-- <h2 style=" font-weight: 750; font-size: 25px;"> {{projectName}} Angelica Portocarrero Quintero</h2> -->
            <router-link to="/Project" style=" font-weight: 750; font-size: 25px; color:black;"> {{projectname}} </router-link>
            <!-- <p> más info </p> -->
        </div>
            <RouterView />
    </div>
</template>

<script>
    export default {
    props: {
        "projectname": String
    }
}
</script>

<style scoped>
    .main-container {
        height: 140px;
        width: 470px;
        background-color: #ffffff;
        border-radius: 24px;
        padding: 20px;
        /* box-shadow: 10px 10px 10px #e3e3e3; */
    }
</style>