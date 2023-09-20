import Vue from 'vue'
import VueRouter from 'vue-router'
import HomePage from '../views/HomePage.vue'
import MonitoringPage from "@/views/MonitoringPage";
import ConfigurationPage from "@/views/ConfigurationPage";
import AdministrationPage from "@/views/AdministrationPage";
import MetersConfPage from "@/views/Config/MetersConfPage";
import ChannelPage from "@/views/Config/ChannelPage";
import DataDayPage from "@/views/Monitor/DataDayPage";
import GroupsPage from "@/views/Config/GroupsPage";
import ChartsPage from "@/views/ChartsPage";
import QueryPage from "@/views/Monitor/QueryPage";
import ObjectPage from "@/views/ObjectPage";

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomePage
    },
    {
        path: '/monitoring',
        name: 'monitoring',
        component: MonitoringPage
    },
    {
        path: '/channels_conf',
        name: 'channels_conf',
        component: ConfigurationPage
    },

    {
        path: '/meters_conf',
        name: 'meters_conf',
        component: MetersConfPage
    },
        {
        path: '/groups_conf',
        name: 'groups_conf',
        component: GroupsPage
    },
    {
        path: '/administration',
        name: 'administration',
        component: AdministrationPage
    },
    {
        path: '/monitorDate',
        name: 'monitorDate',
        component: DataDayPage
    },{
        path: '/queryForm',
        name: 'queryForm',
        component: QueryPage
    },
    {
        path: '/charts',
        name: 'charts',
        component: ChartsPage
    },
    {
        path: '/objects',
        name: 'object_conf',
        component: ObjectPage
    },


]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
