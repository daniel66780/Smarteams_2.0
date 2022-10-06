import { createRouter, createWebHashHistory } from 'vue-router';

// import CreatePage from '../pages/CreatePage.vue'
// import ProfilePage from '../pages/ProfilePage.vue'
// import ProjectPage from '../pages/ProjectPage.vue'
// import RegisterPage from '../pages/RegisterPage.vue'
// import Page404 from '../shared/pages/Page404.vue'

 // este cambio es un lazy load, hace que la app pese menos
const routes = [
    {path: '/', 
    component: () => import('../Pages/HomePage.vue')},
    {path: '/Register', 
    component: () => import('../Pages/RegisterPage.vue')},
    {path: '/Login', 
    component: () => import('../Pages/LoginPage.vue')},
    {path: '/Profile',
    component: () => import('@/Pages/ProfilePage.vue')},
    {path: '/Create',
    component: () => import('@/Pages/CreatePage.vue')},
    {path: '/Project',
    component: () => import('@/Pages/ProjectPage.vue')},
    {path: '/AddTask',
    component: () => import('@/Pages/TaskPage.vue')},
    {path: '/:pathMatch(.*)*',
    component: () => import('@/Pages/Page404.vue')}
]


const router = createRouter({
    history: createWebHashHistory(),
    routes: routes,
})

export default router;