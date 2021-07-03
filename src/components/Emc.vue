<template>
    <div class="col-12 col-md-4">
        <div class="rounded border px-2 py-2">
            <div class="row g-1">
                <div class="col">
                    <div class="row g-1 align-items-baseline justify-content-center">
                        <div class="col-auto d-flex align-items-center">
                            <img :src="require(`../assets/interface/${data[id].source}.png`)" width="12" height="12" />
                        </div>
                        <div class="col-auto text-center">
                            <div class="small">{{ $t(data[id].source) }}</div>
                            <div class="text-light text-uppercase">{{ numeralFormat(sourceCount.toPrecision(4), '0.[000]a') }}</div>
                        </div>
                    </div>
                </div>
                <div class="col-auto">
                    <i class="fas fa-fw fa-long-arrow-alt-right"></i>
                </div>
                <div class="col">
                    <div class="row g-1 align-items-baseline justify-content-center">
                        <div class="col-auto d-flex align-items-center">
                            <img :src="require(`../assets/interface/${data[id].resource}.png`)" width="12" height="12" />
                        </div>
                        <div class="col-auto text-center">
                            <div class="small">{{ $t(data[id].resource) }}</div>
                            <div class="text-light text-uppercase">{{ numeralFormat(destinationCount.toPrecision(4), '0.[000]a') }}</div>
                        </div>
                    </div>
                </div>
                <div class="col-12">
                    <div class="row gx-3 align-items-center">
                        <div v-if="data['autoEmc'].count > 0" class="col-auto">
                            <button class="btn" :class="{ 'btn-outline':autoResource!=id, 'btn-success':autoResource==id }" @click="setAutoEmc(id)">
                                {{ $t('auto') }}
                            </button>
                        </div>
                        <div class="col">
                            <button class="btn w-100" @click="convert(id)">
                                {{ $t('convert') }}
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState, mapActions, mapMutations } from 'vuex'

export default {
    props: [ 'id' ],
    computed: {
        ...mapState([
            'data', 'emcAmount', 'autoResource'
        ]),
        sourceCount: function() {
            if (this.emcAmount == 'max') return Math.max(0, Math.floor((this.data[this.data[this.id].source].count - this.data[this.data[this.id].source].consumption) / this.data[this.id].rate) * this.data[this.id].rate)
            else return Math.min(this.emcAmount, Math.floor(this.data[this.data[this.id].source].count / this.data[this.id].rate)) * this.data[this.id].rate
        },
        destinationCount: function() {
            if (this.emcAmount == 'max') return Math.max(0, Math.floor((this.data[this.data[this.id].source].count - this.data[this.data[this.id].source].consumption) / this.data[this.id].rate))
            else return Math.floor(Math.min(this.emcAmount, this.data[this.data[this.id].source].count / this.data[this.id].rate))
        },
    },
    methods: {
        ...mapMutations([
            'setAutoResource',
        ]),
        ...mapActions([
            'convert',
        ]),
        setAutoEmc(id) {
        
            if (this.autoResource == id) this.setAutoResource(null)
            else this.setAutoResource(id)
        },
    },
}
</script>
