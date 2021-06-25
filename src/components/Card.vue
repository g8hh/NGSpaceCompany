<template>
    <div class="col" role="article">
        <div class="row gx-2 flex-nowrap">
            <div class="col-auto">
                <div class="timeline-marker">
                    <i v-if="!checked" class="fas fa-fw fa-lock-open"></i>
                    <i v-if="checked" class="fas fa-fw fa-check text-success"></i>
                </div>
            </div>
            <div class="col">
                <div class="card card-body">
                    <div class="row g-2">
                        <div v-if="id" class="col-12">
                            <span class="h6 text-light">{{ $t(id) }}</span>
                        </div>
                        <div v-for="desc in descs" :key="desc" class="col-12 small">
                            <span class="text-normal">{{ $t(desc) }}</span>
                        </div>
                        <slot />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: [ 'id', 'descs', 'checked' ],
}
</script>