import { createApp } from 'vue'
// import './style.css'
import App from './App.vue';
import { BootstrapVue3} from 'bootstrap-vue-3'

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'

// Make BootstrapVue available throughout your project

// Optionally install the BootstrapVue icon components plugin

import store from './store';
import router from './router/router';
import './assets/main.css'

createApp(App)
    .use(BootstrapVue3)
    .use(store)
    .use(router)
    .mount('#app')
