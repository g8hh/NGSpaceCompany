<template>
    <div v-if="costs" class="col-12">
        <div class="heading-6">
            <div class="row gx-3">
                <div class="col-auto">
                    {{ $t('costs') }}
                </div>
                <div v-if="mod && mod > 1" class="col-auto">
                    <span class="text-lowercase">x</span>{{ mod }}
                </div>
                <div v-if="id && id == 'segment'" class="col text-end">
                    <button @click="$root.segmentModal.show();" aria-label="Calculator">
                        <i class="fas fa-fw fa-calculator"></i>
                    </button>
                </div>
                <div v-if="id && calc" class="col text-end">
                    <button @click="$root.calcId=id; $root.calcModal.show();" aria-label="Calculator">
                        <i class="fas fa-fw fa-calculator"></i>
                    </button>
                </div>
            </div>
        </div>
        <div v-for="cost in costs" :key="cost.id" class="row g-1">
            <div class="col">
                <button class="text-light small" @click="setActivePane(cost.id + 'Pane')">
                    <div class="row g-1">
                        <div class="col-auto d-flex align-items-center">
                            <img :src="require(`../assets/interface/${cost.id}.png`)" width="12" height="12" :alt="$t(cost.id) + ' icon'" />
                        </div>
                        <div class="col">
                            <span class="text-light">{{ $t(cost.id) }}</span>
                        </div>
                    </div>
                </button>
            </div>
            <div class="col-auto">
                <small v-if="!cost.timer || cost.timer > -2" class="text-uppercase text-light">{{ numeralFormat(cost.count.toPrecision(4), '0.[000]a') }}</small>
                <small v-if="cost.timer <= -2" class="text-uppercase text-danger">{{ numeralFormat(cost.count.toPrecision(4), '0.[000]a') }}</small>
            </div>
            <div class="col-auto text-end" style="width:75px">
                <small v-if="(!cost.timer && cost.timer != 0) || cost.timer < 0" class="text-normal">---</small>
                <small v-if="cost.timer == 0" class="text-success"><i class="fas fa-fw fa-check"></i></small>
                <small v-if="cost.timer > 0 && cost.timer <= (3600 * 24 * 2)" class="text-timer" role="timer">{{ numeralFormat(cost.timer, '00:00:00') }}</small>
                <small v-if="cost.timer > (3600 * 24 * 2)" class="text-timer">{{ $t('bigTimer') }}</small>
            </div>
        </div>
    </div>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
    props: [ 'costs', 'mod', 'id', 'calc' ],
    methods: {
        ...mapMutations([
            'setActivePane',
        ]),
    },
}
</script>