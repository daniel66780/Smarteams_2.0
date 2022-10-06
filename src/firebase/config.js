// Import the functions you need from the SDKs you need
import { getAuth } from "firebase/auth"
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBkvJlNQ_9TTWN2paaV6O-VwxkHgpl9Bng",
  authDomain: "smarteams-678c3.firebaseapp.com",
  projectId: "smarteams-678c3",
  storageBucket: "smarteams-678c3.appspot.com",
  messagingSenderId: "1077615169858",
  appId: "1:1077615169858:web:d75e128107633e4216b8db",
  measurementId: "G-K9EHERJL1P"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth();

export { app, analytics, auth }