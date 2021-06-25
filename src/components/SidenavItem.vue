<template>
    <div v-if="unlocked" class="col">
        <button class="sidenav-item" :class="{ 'active':activePane == id }" @click="setActivePane(id);$root.sidebarOpen = false;">
            <div v-if="isNotif(id)" class="position-absolute top-0 start-0" style="line-height:1">
                <i class="fas fa-fw fa-certificate text-success small"></i>
            </div>
            <div class="row gx-2">
                <div class="col-auto d-flex align-items-center">
                    <img :src="require(`../assets/interface/${icon}`)" width="16" height="16" />
                </div>
                <div class="col">
                    {{ $t(id) }}
                </div>
                <div v-if="prod != null" class="col-auto text-end">
                    <i v-if="problem" class="small me-1 fas fa-fw fa-exclamation-triangle text-danger"></i>
                    <small class="text-uppercase" :class="{ 'text-danger':prod < 0, 'text-normal':prod == 0, 'text-success':prod > 0 }">
                        <span v-if="prod > 0">+</span>{{ numeralFormat(prod.toPrecision(4), '0.[000]a') }}
                    </small>
                    <small class="text-normal ms-1">/s</small>
                </div>
                <div v-if="count != null" class="col-auto text-end" style="width:110px;">
                    <small class="text-uppercase" :class="{ 'text-light':(count > 0 && (!storage || count < storage)), 'text-normal':count == 0, 'text-danger':count < 0, 'text-success':storage && count >= storage }">{{ numeralFormat(count.toPrecision(4), '0.[000]a') }}</small>
                    <small v-if="storage" class="text-uppercase text-normal ms-1">/{{ numeralFormat(storage.toPrecision(4), '0.[000]a') }}</small>
                    <small v-if="potential >= 0" class="text-normal ms-1">({{ potential }})</small>
                </div>
                <div v-if="opinion != null" class="col-auto text-end">
                    <small :class="{ 'text-light':opinion > 0, 'text-normal':opinion == 0, 'text-danger':opinion < 0 }">{{ opinion }}</small>
                </div>
                <div v-if="done" class="col-auto text-end small">
                    <small class="text-success text-uppercase">{{ $t(doneText) }}</small>
                </div>
            </div>
        </button>
    </div>
</template>

<style>
    .sidenav-item {
        position: relative;
        display: block; width: 100%; text-align: left;
        background: transparent; border: 0; border-radius: .25rem;
        padding: .25rem;
        color: #f5f5f5; line-height: 1.5rem; text-decoration: none;
        cursor: pointer;
    }

    .sidenav-item:hover, .sidenav-item:focus, .sidenav-item.active {
        color: #f5f5f5;
        background-color: rgba(255,255,255,.125);
    }
</style>

<script>
import { mapState, mapGetters, mapMutations } from 'vuex'

export default {
    props: [ 'id', 'unlocked', 'icon', 'prod', 'count', 'storage', 'opinion', 'done', 'doneText', 'potential', 'problem' ],
    computed: {
        ...mapState([        
            'activePane',
        ]),
        ...mapGetters([  
            'isNotif',
        ]),
    },
    methods: {
        ...mapMutations([
            'setActivePane',
        ]),
    },
}
</script>