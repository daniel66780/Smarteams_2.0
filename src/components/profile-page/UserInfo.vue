<template>
    <div class="main-container">
        <div class="right-container" style="width: 25%; height: 100%;float:left; ">
            <img src="@/assets/icon-image.png" style="height: 100px; width:100px">
        </div>
        <div class="left-container" style="width: 75%; height: 100%; float:right; ">
            <h2 style=" font-weight: 750; font-size: 25px;"> {{username}}</h2>
            <p> {{useremail}}</p>
        </div>
    </div>
</template>

<script>
    export default {
        props: {
            "username": String,
            "useremail": String
        },
        name: 'UserInfo',
    }
</script>

<style scoped>
    .main-container {
        height: 150px;
        width: 470px;
        background-color: #f1f1f1;
        border-radius: 24px;
        padding: 20px;
        box-shadow: 10px 10px 10px #e3e3e3;
    }
</style>