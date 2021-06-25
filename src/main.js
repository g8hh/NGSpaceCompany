import { createApp } from 'vue'

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

import './assets/styles.css'

import { store } from './store'

import VueNumerals from 'vue-numerals'

import i18n from './i18n.js'

import VueGtag from 'vue-gtag'

import App from './App.vue'

createApp(App)
    .use(store)
    .use(VueNumerals)
    .use(i18n)
    .use(VueGtag, { config: { id:'G-7MZR4NX0GD' } })
    .mount('#app')