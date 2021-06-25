<template>
    <div class="row g-3">
        <div v-if="countTo50 > 0" class="col-12">
            <div class="heading-6">
                <span>{{ $t('costTo50') }}</span>
            </div>
            
            <div class="row g-1">
                <div class="col-auto d-flex align-items-center">
                    <img :src="require(`../assets/interface/titanium.png`)" width="12" height="12" />
                </div>
                <div class="col">
                    <small class="text-light">{{ $t('titanium') }}</small>
                </div>
                <div class="col-auto">
                    <small class="text-uppercase" :class="{ 'text-light':costTo50.titanium.count <= data['titanium'].storage, 'text-danger':costTo50.titanium.count > data['titanium'].storage }">{{ numeralFormat(costTo50.titanium.count.toPrecision(4), '0.[000]a') }}</small>
                </div>
                <div class="col-auto text-end" style="width:75px">
                    <small v-if="data['titanium'].prod <= 0" class="text-normal">---</small>
                    <small v-if="costTo50.titanium.count <= data['titanium'].count" class="text-success"><i class="fas fa-fw fa-check"></i></small>
                    <small v-if="costTo50.titanium.count > data['titanium'].count && costTo50.titanium.timer > (3600 * 24 * 2)" class="text-timer">{{ $t('bigTimer') }}</small>
                    <small v-if="costTo50.titanium.count > data['titanium'].count && costTo50.titanium.timer > 0 && costTo50.titanium.timer <= (3600 * 24 * 2)" class="text-timer" role="timer">{{ numeralFormat(costTo50.titanium.timer, '00:00:00') }}</small>
                </div>                
            </div>
            
            <div class="row g-1">
                <div class="col-auto d-flex align-items-center">
                    <img :src="require(`../assets/interface/gold.png`)" width="12" height="12" />
                </div>
                <div class="col">
                    <small class="text-light">{{ $t('gold') }}</small>
                </div>
                <div class="col-auto">
                    <small class="text-uppercase" :class="{ 'text-light':costTo50.gold.count <= data['gold'].storage, 'text-danger':costTo50.gold.count > data['gold'].storage }">{{ numeralFormat(costTo50.gold.count.toPrecision(4), '0.[000]a') }}</small>
                </div>
                <div class="col-auto text-end" style="width:75px">
                    <small v-if="data['gold'].prod <= 0" class="text-normal">---</small>
                    <small v-if="costTo50.gold.count <= data['gold'].count" class="text-success"><i class="fas fa-fw fa-check"></i></small>
                    <small v-if="costTo50.gold.count > data['gold'].count && costTo50.gold.timer > (3600 * 24 * 2)" class="text-timer">{{ $t('bigTimer') }}</small>
                    <small v-if="costTo50.gold.count > data['gold'].count && costTo50.gold.timer > 0 && costTo50.gold.timer <= (3600 * 24 * 2)" class="text-timer" role="timer">{{ numeralFormat(costTo50.gold.timer, '00:00:00') }}</small>
                </div>                
            </div>
            
            <div class="row g-1">
                <div class="col-auto d-flex align-items-center">
                    <img :src="require(`../assets/interface/silicon.png`)" width="12" height="12" />
                </div>
                <div class="col">
                    <small class="text-light">{{ $t('silicon') }}</small>
                </div>
                <div class="col-auto">
                    <small class="text-uppercase" :class="{ 'text-light':costTo50.silicon.count <= data['silicon'].storage, 'text-danger':costTo50.silicon.count > data['silicon'].storage }">{{ numeralFormat(costTo50.silicon.count.toPrecision(4), '0.[000]a') }}</small>
                </div>
                <div class="col-auto text-end" style="width:75px">
                    <small v-if="data['silicon'].prod <= 0" class="text-normal">---</small>
                    <small v-if="costTo50.silicon.count <= data['silicon'].count" class="text-success"><i class="fas fa-fw fa-check"></i></small>
                    <small v-if="costTo50.silicon.count > data['silicon'].count && costTo50.silicon.timer > (3600 * 24 * 2)" class="text-timer">{{ $t('bigTimer') }}</small>
                    <small v-if="costTo50.silicon.count > data['silicon'].count && costTo50.silicon.timer > 0 && costTo50.silicon.timer <= (3600 * 24 * 2)" class="text-timer" role="timer">{{ numeralFormat(costTo50.silicon.timer, '00:00:00') }}</small>
                </div>                
            </div>

            <div class="row g-1">
                <div class="col-auto d-flex align-items-center">
                    <img :src="require(`../assets/interface/meteorite.png`)" width="12" height="12" />
                </div>
                <div class="col">
                    <small class="text-light">{{ $t('meteorite') }}</small>
                </div>
                <div class="col-auto">
                    <small class="text-uppercase" :class="{ 'text-light':costTo50.meteorite.count <= data['meteorite'].storage, 'text-danger':costTo50.meteorite.count > data['meteorite'].storage }">{{ numeralFormat(costTo50.meteorite.count.toPrecision(4), '0.[000]a') }}</small>
                </div>
                <div class="col-auto text-end" style="width:75px">
                    <small v-if="data['meteorite'].prod <= 0" class="text-normal">---</small>
                    <small v-if="costTo50.meteorite.count <= data['meteorite'].count" class="text-success"><i class="fas fa-fw fa-check"></i></small>
                    <small v-if="costTo50.meteorite.count > data['meteorite'].count && costTo50.meteorite.timer > (3600 * 24 * 2)" class="text-timer">{{ $t('bigTimer') }}</small>
                    <small v-if="costTo50.meteorite.count > data['meteorite'].count && costTo50.meteorite.timer > 0 && costTo50.meteorite.timer <= (3600 * 24 * 2)" class="text-timer" role="timer">{{ numeralFormat(costTo50.meteorite.timer, '00:00:00') }}</small>
                </div>                
            </div>
            
            <div class="row g-1">
                <div class="col-auto d-flex align-items-center">
                    <img :src="require(`../assets/interface/ice.png`)" width="12" height="12" />
                </div>
                <div class="col">
                    <small class="text-light">{{ $t('ice') }}</small>
                </div>
                <div class="col-auto">
                    <small class="text-uppercase" :class="{ 'text-light':costTo50.ice.count <= data['ice'].storage, 'text-danger':costTo50.ice.count > data['ice'].storage }">{{ numeralFormat(costTo50.ice.count.toPrecision(4), '0.[000]a') }}</small>
                </div>
                <div class="col-auto text-end" style="width:75px">
                    <small v-if="data['ice'].prod <= 0" class="text-normal">---</small>
                    <small v-if="costTo50.ice.count <= data['ice'].count" class="text-success"><i class="fas fa-fw fa-check"></i></small>
                    <small v-if="costTo50.ice.count > data['ice'].count && costTo50.ice.timer > (3600 * 24 * 2)" class="text-timer">{{ $t('bigTimer') }}</small>
                    <small v-if="costTo50.ice.count > data['ice'].count && costTo50.ice.timer > 0 && costTo50.ice.timer <= (3600 * 24 * 2)" class="text-timer" role="timer">{{ numeralFormat(costTo50.ice.timer, '00:00:00') }}</small>
                </div>                
            </div>
            
        </div>
        <div v-if="countTo100 > 0" class="col-12">
            <div class="heading-6">
                <span>{{ $t('costTo100') }}</span>
            </div>
            
            <div class="row g-1">
                <div class="col-auto d-flex align-items-center">
                    <img :src="require(`../assets/interface/titanium.png`)" width="12" height="12" />
                </div>
                <div class="col">
                    <small class="text-light">{{ $t('titanium') }}</small>
                </div>
                <div class="col-auto">
                    <small class="text-uppercase" :class="{ 'text-light':costTo100.titanium.count <= data['titanium'].storage, 'text-danger':costTo100.titanium.count > data['titanium'].storage }">{{ numeralFormat(costTo100.titanium.count.toPrecision(4), '0.[000]a') }}</small>
                </div>
                <div class="col-auto text-end" style="width:75px">
                    <small v-if="data['titanium'].prod <= 0" class="text-normal">---</small>
                    <small v-if="costTo100.titanium.count <= data['titanium'].count" class="text-success"><i class="fas fa-fw fa-check"></i></small>
                    <small v-if="costTo100.titanium.count > data['titanium'].count && costTo100.titanium.timer > (3600 * 24 * 2)" class="text-timer">{{ $t('bigTimer') }}</small>
                    <small v-if="costTo100.titanium.count > data['titanium'].count && costTo100.titanium.timer > 0 && costTo100.titanium.timer <= (3600 * 24 * 2)" class="text-timer" role="timer">{{ numeralFormat(costTo100.titanium.timer, '00:00:00') }}</small>
                </div>                
            </div>
            
            <div class="row g-1">
                <div class="col-auto d-flex align-items-center">
                    <img :src="require(`../assets/interface/gold.png`)" width="12" height="12" />
                </div>
                <div class="col">
                    <small class="text-light">{{ $t('gold') }}</small>
                </div>
                <div class="col-auto">
                    <small class="text-uppercase" :class="{ 'text-light':costTo100.gold.count <= data['gold'].storage, 'text-danger':costTo100.gold.count > data['gold'].storage }">{{ numeralFormat(costTo100.gold.count.toPrecision(4), '0.[000]a') }}</small>
                </div>
                <div class="col-auto text-end" style="width:75px">
                    <small v-if="data['gold'].prod <= 0" class="text-normal">---</small>
                    <small v-if="costTo100.gold.count <= data['gold'].count" class="text-success"><i class="fas fa-fw fa-check"></i></small>
                    <small v-if="costTo100.gold.count > data['gold'].count && costTo100.gold.timer > (3600 * 24 * 2)" class="text-timer">{{ $t('bigTimer') }}</small>
                    <small v-if="costTo100.gold.count > data['gold'].count && costTo100.gold.timer > 0 && costTo100.gold.timer <= (3600 * 24 * 2)" class="text-timer" role="timer">{{ numeralFormat(costTo100.gold.timer, '00:00:00') }}</small>
                </div>                
            </div>
            
            <div class="row g-1">
                <div class="col-auto d-flex align-items-center">
                    <img :src="require(`../assets/interface/silicon.png`)" width="12" height="12" />
                </div>
                <div class="col">
                    <small class="text-light">{{ $t('silicon') }}</small>
                </div>
                <div class="col-auto">
                    <small class="text-uppercase" :class="{ 'text-light':costTo100.silicon.count <= data['silicon'].storage, 'text-danger':costTo100.silicon.count > data['silicon'].storage }">{{ numeralFormat(costTo100.silicon.count.toPrecision(4), '0.[000]a') }}</small>
                </div>
                <div class="col-auto text-end" style="width:75px">
                    <small v-if="data['silicon'].prod <= 0" class="text-normal">---</small>
                    <small v-if="costTo100.silicon.count <= data['silicon'].count" class="text-success"><i class="fas fa-fw fa-check"></i></small>
                    <small v-if="costTo100.silicon.count > data['silicon'].count && costTo100.silicon.timer > (3600 * 24 * 2)" class="text-timer">{{ $t('bigTimer') }}</small>
                    <small v-if="costTo100.silicon.count > data['silicon'].count && costTo100.silicon.timer > 0 && costTo100.silicon.timer <= (3600 * 24 * 2)" class="text-timer" role="timer">{{ numeralFormat(costTo100.silicon.timer, '00:00:00') }}</small>
                </div>                
            </div>

            <div class="row g-1">
                <div class="col-auto d-flex align-items-center">
                    <img :src="require(`../assets/interface/meteorite.png`)" width="12" height="12" />
                </div>
                <div class="col">
                    <small class="text-light">{{ $t('meteorite') }}</small>
                </div>
                <div class="col-auto">
                    <small class="text-uppercase" :class="{ 'text-light':costTo100.meteorite.count <= data['meteorite'].storage, 'text-danger':costTo100.meteorite.count > data['meteorite'].storage }">{{ numeralFormat(costTo100.meteorite.count.toPrecision(4), '0.[000]a') }}</small>
                </div>
                <div class="col-auto text-end" style="width:75px">
                    <small v-if="data['meteorite'].prod <= 0" class="text-normal">---</small>
                    <small v-if="costTo100.meteorite.count <= data['meteorite'].count" class="text-success"><i class="fas fa-fw fa-check"></i></small>
                    <small v-if="costTo100.meteorite.count > data['meteorite'].count && costTo100.meteorite.timer > (3600 * 24 * 2)" class="text-timer">{{ $t('bigTimer') }}</small>
                    <small v-if="costTo100.meteorite.count > data['meteorite'].count && costTo100.meteorite.timer > 0 && costTo100.meteorite.timer <= (3600 * 24 * 2)" class="text-timer" role="timer">{{ numeralFormat(costTo100.meteorite.timer, '00:00:00') }}</small>
                </div>                
            </div>
            
            <div class="row g-1">
                <div class="col-auto d-flex align-items-center">
                    <img :src="require(`../assets/interface/ice.png`)" width="12" height="12" />
                </div>
                <div class="col">
                    <small class="text-light">{{ $t('ice') }}</small>
                </div>
                <div class="col-auto">
                    <small class="text-uppercase" :class="{ 'text-light':costTo100.ice.count <= data['ice'].storage, 'text-danger':costTo100.ice.count > data['ice'].storage }">{{ numeralFormat(costTo100.ice.count.toPrecision(4), '0.[000]a') }}</small>
                </div>
                <div class="col-auto text-end" style="width:75px">
                    <small v-if="data['ice'].prod <= 0" class="text-normal">---</small>
                    <small v-if="costTo100.ice.count <= data['ice'].count" class="text-success"><i class="fas fa-fw fa-check"></i></small>
                    <small v-if="costTo100.ice.count > data['ice'].count && costTo100.ice.timer > (3600 * 24 * 2)" class="text-timer">{{ $t('bigTimer') }}</small>
                    <small v-if="costTo100.ice.count > data['ice'].count && costTo100.ice.timer > 0 && costTo100.ice.timer <= (3600 * 24 * 2)" class="text-timer" role="timer">{{ numeralFormat(costTo100.ice.timer, '00:00:00') }}</small>
                </div>                
            </div>
            
        </div>
        <div v-if="countTo250 > 0" class="col-12">
            <div class="heading-6">
                <span>{{ $t('costTo250') }}</span>
            </div>
            
            <div class="row g-1">
                <div class="col-auto d-flex align-items-center">
                    <img :src="require(`../assets/interface/titanium.png`)" width="12" height="12" />
                </div>
                <div class="col">
                    <small class="text-light">{{ $t('titanium') }}</small>
                </div>
                <div class="col-auto">
                    <small class="text-uppercase" :class="{ 'text-light':costTo250.titanium.count <= data['titanium'].storage, 'text-danger':costTo250.titanium.count > data['titanium'].storage }">{{ numeralFormat(costTo250.titanium.count.toPrecision(4), '0.[000]a') }}</small>
                </div>
                <div class="col-auto text-end" style="width:75px">
                    <small v-if="data['titanium'].prod <= 0" class="text-normal">---</small>
                    <small v-if="costTo250.titanium.count <= data['titanium'].count" class="text-success"><i class="fas fa-fw fa-check"></i></small>
                    <small v-if="costTo250.titanium.count > data['titanium'].count && costTo250.titanium.timer > (3600 * 24 * 2)" class="text-timer">{{ $t('bigTimer') }}</small>
                    <small v-if="costTo250.titanium.count > data['titanium'].count && costTo250.titanium.timer > 0 && costTo250.titanium.timer <= (3600 * 24 * 2)" class="text-timer" role="timer">{{ numeralFormat(costTo250.titanium.timer, '00:00:00') }}</small>
                </div>                
            </div>
            
            <div class="row g-1">
                <div class="col-auto d-flex align-items-center">
                    <img :src="require(`../assets/interface/gold.png`)" width="12" height="12" />
                </div>
                <div class="col">
                    <small class="text-light">{{ $t('gold') }}</small>
                </div>
                <div class="col-auto">
                    <small class="text-uppercase" :class="{ 'text-light':costTo250.gold.count <= data['gold'].storage, 'text-danger':costTo250.gold.count > data['gold'].storage }">{{ numeralFormat(costTo250.gold.count.toPrecision(4), '0.[000]a') }}</small>
                </div>
                <div class="col-auto text-end" style="width:75px">
                    <small v-if="data['gold'].prod <= 0" class="text-normal">---</small>
                    <small v-if="costTo250.gold.count <= data['gold'].count" class="text-success"><i class="fas fa-fw fa-check"></i></small>
                    <small v-if="costTo250.gold.count > data['gold'].count && costTo250.gold.timer > (3600 * 24 * 2)" class="text-timer">{{ $t('bigTimer') }}</small>
                    <small v-if="costTo250.gold.count > data['gold'].count && costTo250.gold.timer > 0 && costTo250.gold.timer <= (3600 * 24 * 2)" class="text-timer" role="timer">{{ numeralFormat(costTo250.gold.timer, '00:00:00') }}</small>
                </div>                
            </div>
            
            <div class="row g-1">
                <div class="col-auto d-flex align-items-center">
                    <img :src="require(`../assets/interface/silicon.png`)" width="12" height="12" />
                </div>
                <div class="col">
                    <small class="text-light">{{ $t('silicon') }}</small>
                </div>
                <div class="col-auto">
                    <small class="text-uppercase" :class="{ 'text-light':costTo250.silicon.count <= data['silicon'].storage, 'text-danger':costTo250.silicon.count > data['silicon'].storage }">{{ numeralFormat(costTo250.silicon.count.toPrecision(4), '0.[000]a') }}</small>
                </div>
                <div class="col-auto text-end" style="width:75px">
                    <small v-if="data['silicon'].prod <= 0" class="text-normal">---</small>
                    <small v-if="costTo250.silicon.count <= data['silicon'].count" class="text-success"><i class="fas fa-fw fa-check"></i></small>
                    <small v-if="costTo250.silicon.count > data['silicon'].count && costTo250.silicon.timer > (3600 * 24 * 2)" class="text-timer">{{ $t('bigTimer') }}</small>
                    <small v-if="costTo250.silicon.count > data['silicon'].count && costTo250.silicon.timer > 0 && costTo250.silicon.timer <= (3600 * 24 * 2)" class="text-timer" role="timer">{{ numeralFormat(costTo250.silicon.timer, '00:00:00') }}</small>
                </div>                
            </div>

            <div class="row g-1">
                <div class="col-auto d-flex align-items-center">
                    <img :src="require(`../assets/interface/meteorite.png`)" width="12" height="12" />
                </div>
                <div class="col">
                    <small class="text-light">{{ $t('meteorite') }}</small>
                </div>
                <div class="col-auto">
                    <small class="text-uppercase" :class="{ 'text-light':costTo250.meteorite.count <= data['meteorite'].storage, 'text-danger':costTo250.meteorite.count > data['meteorite'].storage }">{{ numeralFormat(costTo250.meteorite.count.toPrecision(4), '0.[000]a') }}</small>
                </div>
                <div class="col-auto text-end" style="width:75px">
                    <small v-if="data['meteorite'].prod <= 0" class="text-normal">---</small>
                    <small v-if="costTo250.meteorite.count <= data['meteorite'].count" class="text-success"><i class="fas fa-fw fa-check"></i></small>
                    <small v-if="costTo250.meteorite.count > data['meteorite'].count && costTo250.meteorite.timer > (3600 * 24 * 2)" class="text-timer">{{ $t('bigTimer') }}</small>
                    <small v-if="costTo250.meteorite.count > data['meteorite'].count && costTo250.meteorite.timer > 0 && costTo250.meteorite.timer <= (3600 * 24 * 2)" class="text-timer" role="timer">{{ numeralFormat(costTo250.meteorite.timer, '00:00:00') }}</small>
                </div>                
            </div>
            
            <div class="row g-1">
                <div class="col-auto d-flex align-items-center">
                    <img :src="require(`../assets/interface/ice.png`)" width="12" height="12" />
                </div>
                <div class="col">
                    <small class="text-light">{{ $t('ice') }}</small>
                </div>
                <div class="col-auto">
                    <small class="text-uppercase" :class="{ 'text-light':costTo250.ice.count <= data['ice'].storage, 'text-danger':costTo250.ice.count > data['ice'].storage }">{{ numeralFormat(costTo250.ice.count.toPrecision(4), '0.[000]a') }}</small>
                </div>
                <div class="col-auto text-end" style="width:75px">
                    <small v-if="data['ice'].prod <= 0" class="text-normal">---</small>
                    <small v-if="costTo250.ice.count <= data['ice'].count" class="text-success"><i class="fas fa-fw fa-check"></i></small>
                    <small v-if="costTo250.ice.count > data['ice'].count && costTo250.ice.timer > (3600 * 24 * 2)" class="text-timer">{{ $t('bigTimer') }}</small>
                    <small v-if="costTo250.ice.count > data['ice'].count && costTo250.ice.timer > 0 && costTo250.ice.timer <= (3600 * 24 * 2)" class="text-timer" role="timer">{{ numeralFormat(costTo250.ice.timer, '00:00:00') }}</small>
                </div>                
            </div>
            
        </div>
    </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
    computed: {
        ...mapState([
            'data',
        ]),

        countTo50: function() { return 50 - this.data['segment'].count },
        countTo100: function() { return 100 - this.data['segment'].count },
        countTo250: function() { return 250 - this.data['segment'].count },

        costTo50: function() {
        
            let costTitanium  = this.computeCost(this.data['segment'].baseCosts[0].count, 50) - this.computeCost(this.data['segment'].baseCosts[0].count, this.data['segment'].count)
            let costGold      = this.computeCost(this.data['segment'].baseCosts[1].count, 50) - this.computeCost(this.data['segment'].baseCosts[1].count, this.data['segment'].count)
            let costSilicon   = this.computeCost(this.data['segment'].baseCosts[2].count, 50) - this.computeCost(this.data['segment'].baseCosts[2].count, this.data['segment'].count)
            let costMeteorite = this.computeCost(this.data['segment'].baseCosts[3].count, 50) - this.computeCost(this.data['segment'].baseCosts[3].count, this.data['segment'].count)
            let costIce       = this.computeCost(this.data['segment'].baseCosts[4].count, 50) - this.computeCost(this.data['segment'].baseCosts[4].count, this.data['segment'].count)
            
            return {
                titanium:  { count: costTitanium,  timer: this.data['titanium'].prod > 0 ? (costTitanium - this.data['titanium'].count) / this.data['titanium'].prod : 0    },
                gold:      { count: costGold,      timer: this.data['gold'].prod > 0 ? (costGold - this.data['gold'].count) / this.data['gold'].prod : 0                },
                silicon:   { count: costSilicon,   timer: this.data['silicon'].prod > 0 ? (costSilicon - this.data['silicon'].count) / this.data['silicon'].prod : 0       },
                meteorite: { count: costMeteorite, timer: this.data['meteorite'].prod > 0 ? (costMeteorite - this.data['meteorite'].count) / this.data['meteorite'].prod : 0 },
                ice:       { count: costIce,       timer: this.data['ice'].prod > 0 ? (costIce - this.data['ice'].count) / this.data['ice'].prod : 0                   },
            }
        },
        costTo100: function() {
        
            let costTitanium  = this.computeCost(this.data['segment'].baseCosts[0].count, 100) - this.computeCost(this.data['segment'].baseCosts[0].count, this.data['segment'].count)
            let costGold      = this.computeCost(this.data['segment'].baseCosts[1].count, 100) - this.computeCost(this.data['segment'].baseCosts[1].count, this.data['segment'].count)
            let costSilicon   = this.computeCost(this.data['segment'].baseCosts[2].count, 100) - this.computeCost(this.data['segment'].baseCosts[2].count, this.data['segment'].count)
            let costMeteorite = this.computeCost(this.data['segment'].baseCosts[3].count, 100) - this.computeCost(this.data['segment'].baseCosts[3].count, this.data['segment'].count)
            let costIce       = this.computeCost(this.data['segment'].baseCosts[4].count, 100) - this.computeCost(this.data['segment'].baseCosts[4].count, this.data['segment'].count)
            
            return {
                titanium:  { count: costTitanium,  timer: this.data['titanium'].prod > 0 ? (costTitanium - this.data['titanium'].count) / this.data['titanium'].prod : 0    },
                gold:      { count: costGold,      timer: this.data['gold'].prod > 0 ? (costGold - this.data['gold'].count) / this.data['gold'].prod : 0                },
                silicon:   { count: costSilicon,   timer: this.data['silicon'].prod > 0 ? (costSilicon - this.data['silicon'].count) / this.data['silicon'].prod : 0       },
                meteorite: { count: costMeteorite, timer: this.data['meteorite'].prod > 0 ? (costMeteorite - this.data['meteorite'].count) / this.data['meteorite'].prod : 0 },
                ice:       { count: costIce,       timer: this.data['ice'].prod > 0 ? (costIce - this.data['ice'].count) / this.data['ice'].prod : 0                   },
            }
        },
        costTo250: function() {
        
            let costTitanium  = this.computeCost(this.data['segment'].baseCosts[0].count, 250) - this.computeCost(this.data['segment'].baseCosts[0].count, this.data['segment'].count)
            let costGold      = this.computeCost(this.data['segment'].baseCosts[1].count, 250) - this.computeCost(this.data['segment'].baseCosts[1].count, this.data['segment'].count)
            let costSilicon   = this.computeCost(this.data['segment'].baseCosts[2].count, 250) - this.computeCost(this.data['segment'].baseCosts[2].count, this.data['segment'].count)
            let costMeteorite = this.computeCost(this.data['segment'].baseCosts[3].count, 250) - this.computeCost(this.data['segment'].baseCosts[3].count, this.data['segment'].count)
            let costIce       = this.computeCost(this.data['segment'].baseCosts[4].count, 250) - this.computeCost(this.data['segment'].baseCosts[4].count, this.data['segment'].count)
            
            return {
                titanium:  { count: costTitanium,  timer: this.data['titanium'].prod > 0 ? (costTitanium - this.data['titanium'].count) / this.data['titanium'].prod : 0    },
                gold:      { count: costGold,      timer: this.data['gold'].prod > 0 ? (costGold - this.data['gold'].count) / this.data['gold'].prod : 0                },
                silicon:   { count: costSilicon,   timer: this.data['silicon'].prod > 0 ? (costSilicon - this.data['silicon'].count) / this.data['silicon'].prod : 0       },
                meteorite: { count: costMeteorite, timer: this.data['meteorite'].prod > 0 ? (costMeteorite - this.data['meteorite'].count) / this.data['meteorite'].prod : 0 },
                ice:       { count: costIce,       timer: this.data['ice'].prod > 0 ? (costIce - this.data['ice'].count) / this.data['ice'].prod : 0                   },
            }
        },
    },
    methods: {
        computeCost(base, n) {
            return Math.floor(base * (1 - Math.pow(1.02, n)) / (1 - 1.02))
        },
    },
}
</script>