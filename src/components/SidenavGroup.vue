<template>
    <div v-if="unlocked" class="col">
        <button class="sidenav-group" :class="{ 'collapsed':isCollapsed(id) }" data-bs-toggle="collapse" :data-bs-target="'#collapse' + id" role="heading" @click="toggleCollapsed(id)">
            {{ $t(id) }}
        </button>
        <div :id="'collapse' + id" class="collapse row gx-2 gy-1 row-cols-1" :class="{ 'show':!isCollapsed(id) }">
            <slot></slot>
        </div>
    </div>
</template>

<style>
    .sidenav-group {
        color: #8c949a; font-size: .75rem; text-transform: uppercase;
        width: 100%; padding: 0 0 .25rem;
        background: transparent; border: 0;
        cursor: pointer;
        display: flex; justify-content: space-between;
    }

    .sidenav-group:hover {
        color: #f5f5f5;
    }

    .sidenav-group::after {
        font-weight: 900; font-family: "Font Awesome 5 Free";
        width: 1.25em;
        content: "\f104";
        transition: transform .25s ease-out;
    }

    .sidenav-group:not(.collapsed)::after {
        transform: rotate(-90deg);
    }
</style>

<script>
import { mapGetters, mapMutations } from 'vuex'

export default {
    props: [ 'id', 'unlocked' ],
    computed: {
        ...mapGetters([
            'isCollapsed'
        ]),
    },
    methods: {
        ...mapMutations([
            'toggleCollapsed',
        ]),
    },
}
</script>