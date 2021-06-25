<template>
    <div class="col">
        <div class="row gx-2">
            <div class="col-auto">
                <div class="timeline-marker">
                
                    <i class="fas fa-fw fa-lock-open"></i>
                    
                </div>
            </div>
            <div class="col">            
                <div class="card card-body">
                    <div class="row g-3">
                        <div class="col-12 col-md-6">
                            <div class="row g-3">
                            
                                <div class="col-12">
                                    <span class="h6 text-light">{{ $t(id) }}</span>
                                </div>
                                                            
                            </div>
                        </div>
                        <div class="col-12 col-md-6">
                            <div class="row g-3">
                            
                                <div class="col-12">
                                    <div class="heading-6">{{ $t('stats') }}</div>
                                    <div class="row g-1 gx-3">
                                        <div class="col-auto">
                                            <span class="small text-normal">{{ $t('power') }}</span>
                                            <span class="ms-2 text-light">{{ numeralFormat(fleet.power, '0.[0]a') }}</span>
                                        </div>
                                        <div class="col-auto">
                                            <span class="small text-normal">{{ $t('defense') }}</span>
                                            <span class="ms-2 text-light">{{ numeralFormat(fleet.defense, '0.[0]a') }}</span>
                                        </div>
                                        <div class="col-auto">
                                            <span class="small text-normal">{{ $t('speed') }}</span>
                                            <span class="ms-2 text-light">{{ numeralFormat(fleet.speed, '0.[0]a') }}</span>
                                        </div>
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
import { mapState } from 'vuex'

export default {
    props: [ 'id' ],
    computed: mapState([
        'fleet',
    ]),
}
</script>
