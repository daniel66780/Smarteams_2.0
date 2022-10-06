<template>
    <div class="main-container">
        <div class="right-container" style="width: 25%; height: 100%;float:left; ">
            <img src="@/assets/icon-image.png" style="height: 70px; width:70px">
        </div>
        <div class="left-container" style="width: 75%; height: 100%; float:right; ">
            <!-- <h2 style=" font-weight: 750; font-size: 25px;"> {{username}}</h2> -->
            <router-link to="/Profile" style=" font-weight: 750; font-size: 25px; color:black;"> {{username}} </router-link>
            <p> {{role}}</p>
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            "username": String,
            "role": String
        },
        name: 'TeamUsers',
    }
</script>

<style scoped>
    .main-container {
        height: 100px;
        width: 450px;
        /* background-color: #f7f7f7; */
        background-color: #ffffff;
        color:#000;
        border-radius: 24px;
        padding: 20px;
        /* box-shadow: 10px 10px 10px #f0f0f0; */
    }
</style>