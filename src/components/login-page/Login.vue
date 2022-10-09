<template>
    <div class="container">
        <div v-if="error" class="alert alert-danger"> {{error}} </div>
        <form @submit.prevent="login()">
            <div class="mb-3">
                <label for="email" class="form-label">
                    Ingrese su correo electrónico
                </label>
                <input 
                    id="email" type="email" class="form-control"
                    name="email" required autofocus v-model="email"                
                >
            </div>

            <div class="mb-3">
                <label for="password" class="form-label"> Ingrese su contraseña </label>
                <input 
                    id="password" type="password" class="form-control"
                    name="password" required v-model="password"                
                >
            </div>

            <div class="form-group row mb-0">
                <div class="col-md-8 offset-md-4">
                    <button type="submit" class="btn btn-primary">Con este boton se suben los datos</button>
                    <router-link to="/Profile" class="btn"> Con este se pasa la pagina del router </router-link>
                </div>
            </div>
        </form>
    <!-- <router-link to="/Profile" @click="login()" class="btn"> Acceder </router-link>
    <RouterView /> -->
    </div>
</template>

<script>
import {useStore} from 'vuex'
import {useRouter} from 'vue-router'

export default {
    name: 'Login',
    data(){
      return{
          
          email:"",
          error: null,
          password: "",
          store: useStore,
          router: useRouter    
      }
    },
    methods:{
        async login(){
            try {
                await this.store.dispatch('user/logIn', {
                    email: this.email,
                    password: this.password
            })
            router.push('/')
            }
            catch (err){
                this.error =err.message
            }
        }
    },
    mounted(){
        onAuthStateChanged(auth, async(user) =>{
            if (!user) return this.store.dispatch("user/logout");

            await this.store.dispatch('user/logIn', {
                email:this.email,
                password: this.password
            })
        })
    }
}
</script>

<style scoped>
.p{
    font-weight: 800;
    font-size: 20px
}
.btn{
  width: 200px;
  background-color: #FF5758;
  color: #ffffff;
  padding: 10px 20px;
  margin: 10px 0;
  border: none;
  border-radius: 24px;
  cursor: pointer;
  font-weight: 750;
  font-size: 18px;
  text-align:center;
  display: inline-block;
}
.field{
  width: 250px;
  background-color: #EBE9E9;
  color: #5c5c5c;
  padding: 10px 17px;
  margin: 10px 0;
  border: none;
  border-radius: 24px;
  cursor: text;
}
</style>