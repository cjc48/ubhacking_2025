// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyDfEJ9nuvUTHdYMbaPwHtI-DTZ50NfwcSw",
    authDomain: "ubh2025-9759a.firebaseapp.com",
    projectId: "ubh2025-9759a",
    storageBucket: "ubh2025-9759a.firebasestorage.app",
    messagingSenderId: "999049594533",
    appId: "1:999049594533:web:cb394b0e94ebccfcaaaf4c",
    measurementId: "G-TCCR0CFTBQ"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const db = getDatabase(app);
const analytics = getAnalytics(app);