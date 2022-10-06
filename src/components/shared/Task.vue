<template>
    <div class="main-container" >
        <input class="form-check-input" type="checkbox" value="" id="task">
        <label class="form-check-label" for="task">
            <h2 style=" font-weight: 750; font-size: 25px;"> {{TaskName}} </h2>
            <p> fecha límite: {{deadline}} <br/>  {{taskUser}} </p>
        </label>
    </div>
    
</template>

<script>
    export default {
        props: {
            "TaskName": String,
            "taskUser": String,
            "deadline": String
        },
        name: 'Task',
    }
</script>

<style scoped>
    .main-container {
        height: 120px;
        width: 450px;
        background-color: #f1f1f1;
        color:#000000;
        border-radius: 24px;
        padding: 13px 20px;
        /* box-shadow: 10px 10px 10px #e3e3e3; */
    }
</style>