<template>
    <div v-for="bracket in brackets" :key="bracket" class="mt-3">        
        <div v-if="countTo(bracket) > 0" class="col-12">        
            <div class="heading-6">
                <span>{{ $t('costTo' + bracket) }}</span>
            </div>
            <div v-for="cost in data[id].baseCosts" :key="cost.id" class="row g-1">
                <div class="col-auto d-flex align-items-center">
                    <img :src="require(`../assets/interface/${cost.id}.png`)" width="12" height="12" />
                </div>
                <div class="col">
                    <small class="text-light">{{ $t(cost.id) }}</small>
                </div>
                <div class="col-auto">
                    <small class="text-uppercase" :class="{ 'text-light':costTo(bracket, cost.count, data[id].count, id) <= data[cost.id].storage, 'text-excess':costTo(bracket, cost.count, data[id].count, id) <= getStorageCap(cost.id) && costTo(bracket, cost.count, data[id].count, id) > data[cost.id].storage, 'text-danger':costTo(bracket, cost.count, data[id].count, id) > getStorageCap(cost.id) }">{{ numeralFormat(costTo(bracket, cost.count, data[id].count, id).toPrecision(4), '0.[000]a') }}</small>
                </div>
                <div class="col-auto text-end" style="width:75px">
                    <small v-if="data[cost.id].prod <= 0" class="text-normal">---</small>
                    <small v-if="costTo(bracket, cost.count, data[id].count, id) <= data[cost.id].count" class="text-success"><i class="fas fa-fw fa-check"></i></small>
                    <small v-if="costTo(bracket, cost.count, data[id].count, id) > data[cost.id].count && timerTo(bracket, cost.count, data[id].count, cost.id) > (3600 * 24 * 2)" class="text-timer">{{ $t('bigTimer') }}</small>
                    <small v-if="costTo(bracket, cost.count, data[id].count, id) > data[cost.id].count && timerTo(bracket, cost.count, data[id].count, cost.id) > 0 && timerTo(bracket, cost.count, data[id].count, cost.id) <= (3600 * 24 * 2)" class="text-timer" role="timer">{{ numeralFormat(timerTo(bracket, cost.count, data[id].count, cost.id), '00:00:00') }}</small>
                </div>                
            </div>
        </div>
    </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex'

export default {
    props: [ 'id' ],
    computed: {
        ...mapState([
            'data',
        ]),
        ...mapGetters([
        
            'getStorageCap',
        ]),
        brackets() {
            if (this.id == 'shield') return [50]
            else if (this.id == 'engine') return [25]
            else if (this.id == 'aero') return [15]
            else return [5, 25, 75, 150, 250]
        },
    },
    methods: {
        countTo(limit) {
            return limit - this.data[this.id].count 
        },
        computeCost(base, n) {
            return Math.floor(base * (1 - Math.pow(1.1, n)) / (1 - 1.1))
        },
        costTo(n, base, current, id) {
            let cost = this.computeCost(base, n) - this.computeCost(base, current)
            if (this.data[id].titan == true) cost *= 0.1
            return cost
        },
        timerTo(n, base, current, id) {
            let cost = this.costTo(n, base, current, id)
            return this.data[id].prod > 0 ? (cost - this.data[id].count) / this.data[id].prod : 0
        },
    },
}
</script>