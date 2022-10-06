<template>
    <div>
      <md-progress-bar md-mode="determinate" :md-value="amount"></md-progress-bar>
      <md-progress-bar class="md-accent" md-mode="determinate" :md-value="amount"></md-progress-bar>
      <p> {{ amount }}% completado </p>
      <input type="range" v-model.number="amount">
    </div>
  </template>
  
  <script>
    export default {
      name: 'ProgressBar',
      data: () => ({
        amount: 0
      })
    }
  </script>
  
  <style scoped>
    .md-progress-bar {
      margin: 24px;
    }
  </style>