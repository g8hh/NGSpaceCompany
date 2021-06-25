<template>
    <div class="col">
        <div class="row gx-2">
            <div class="col-auto">
                <div class="timeline-marker">
                
                    <i v-if="!data[id].unlocked" class="fas fa-fw fa-lock text-muted"></i>
                    <i v-if="data[id].unlocked && data[id].status != 'owned'" class="fas fa-fw fa-lock-open"></i>
                    <i v-if="data[id].unlocked && data[id].status == 'owned'" class="fas fa-fw fa-check text-success"></i>
                    
                </div>
            </div>
            <div class="col">
            
                <div v-if="!data[id].unlocked" class="card card-body">
                    <span class="text-muted">{{ $t('locked') }}</span>
                </div>
                
                <div v-if="data[id].unlocked && data[id].status == 'owned'" class="card card-body">
                    <div class="row g-1">
                        <div class="col-12">
                            <span class="h6 text-light mb-0">{{ $t(data[id].id) }}</span>
                        </div>
                        <div class="col-12 small">
                            <div class="row gy-2 gx-3">
                                <div class="col-auto text-light"> 
                                    <div class="row g-1 align-items-center">
                                        <div class="col-auto d-flex align-items-center">
                                            <img :src="require(`../assets/interface/${data[id].resource1}.png`)" width="12" height="12" />
                                        </div>
                                        <div class="col-auto">
                                            <span class="text-normal">{{ $t(data[id].resource1) }}</span>
                                        </div>
                                        <div class="col-auto small">
                                            <span class="text-success">+25%</span>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-auto text-light">
                                    <div class="row g-1 align-items-center">
                                        <div class="col-auto d-flex align-items-center">
                                            <img :src="require(`../assets/interface/${data[id].resource2}.png`)" width="12" height="12" />
                                        </div>
                                        <div class="col-auto">
                                            <span class="text-normal">{{ $t(data[id].resource2) }}</span>
                                        </div>
                                        <div class="col-auto small">
                                            <span class="text-success">+25%</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div v-if="data[id].unlocked && data[id].status != 'owned'" class="card card-body">
                    <div class="row g-3">
                        <div class="col-12 col-md-6">
                            <div class="row g-3">
                            
                                <div class="col-12">
                                    <span class="h6 text-light">{{ $t(data[id].id) }}</span>
                                </div>
                                <div class="col-12 small">
                                    <div>
                                        <span class="text-normal">{{ $t('distance') }}</span>
                                        <span class="ms-2 text-light">{{ data[id].distance }}</span>
                                    </div>
                                    <div>
                                        <span class="text-normal">{{ $t('planets') }}</span>
                                        <span class="ms-2 text-light">{{ data[id].planets }}</span>
                                    </div>
                                </div>
                                <div class="col-12 small">
                                    <div class="row gy-2 gx-3">
                                        <div class="col-auto text-light"> 
                                            <div class="row g-1">
                                                <div class="col-auto d-flex align-items-center">
                                                    <img :src="require(`../assets/interface/${data[id].resource1}.png`)" width="12" height="12" />
                                                </div>
                                                <div class="col-auto">
                                                    <span class="text-normal">{{ $t(data[id].resource1) }}</span>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-auto text-light">
                                            <div class="row g-1">
                                                <div class="col-auto d-flex align-items-center">
                                                    <img :src="require(`../assets/interface/${data[id].resource2}.png`)" width="12" height="12" />
                                                </div>
                                                <div class="col-auto">
                                                    <span class="text-normal">{{ $t(data[id].resource2) }}</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                
                            </div>
                        </div>
                        <div class="col-12 col-md-6">
                            <div class="row g-3">
                            
                                <costs v-if="data[id].count == 0" :costs="data[id].costs" />
                                
                                <div v-if="data[id].count > 0" class="col-12">
                                    <div class="heading-6">{{ $t('stats') }}</div>
                                    <div class="row g-1 gx-3">
                                        <div class="col-auto">
                                            <span class="small text-normal">{{ $t('power') }}</span>
                                            <span class="ms-2 text-light">{{ getStarPower(id) }}</span>
                                        </div>
                                        <div class="col-auto">
                                            <span class="small text-normal">{{ $t('defense') }}</span>
                                            <span class="ms-2 text-light">{{ getStarDefense(id) }}</span>
                                        </div>
                                        <div class="col-auto">
                                            <span class="small text-normal">{{ $t('speed') }}</span>
                                            <span class="ms-2 text-light">{{ getStarSpeed(id) }}</span>
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="col-12">
                                    <div class="row gx-1 gy-3 justify-content-end">
                                        <div v-if="data[id].count == 0" class="col-auto"><button class="btn" @click="build({id:id, count:1})">{{ $t('explore') }}</button></div>
                                        <div v-if="data[id].count > 0" class="col-auto"><button class="btn" @click="$root.activeStar = id; $root.spyModal.show();">{{ $t('spy') }}</button></div>
                                        <div v-if="data[id].count > 0" class="col-auto"><button class="btn" @click="$root.activeStar = id; $root.invadeModal.show();">{{ $t('invade') }}</button></div>
                                        <div v-if="data[id].count > 0" class="col-auto"><button class="btn" @click="$root.activeStar = id; $root.absorbModal.show();">{{ $t('absorb') }}</button></div>
                                    </div>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                </div>
                
            </div>
        </div>
    </div>
</template>

<script>
import Costs from './Costs.vue'

import { mapState, mapGetters, mapActions } from 'vuex'

export default {
    props: [ 'id' ],
    components: {
        'costs': Costs,
    },
    computed: {
        ...mapState([
            'data',
        ]),
        ...mapGetters([
            'getStarPower', 'getStarDefense', 'getStarSpeed',
        ]),
    },
    methods: {
        ...mapActions([
            'build',
        ]),
    },
}
</script>