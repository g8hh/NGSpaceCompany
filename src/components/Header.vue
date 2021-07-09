<template>
    <div class="header" role="heading" aria-level="1">
        <div class="row gx-3 align-items-center h-100">
            <slot />
        </div>
    </div>
</template>

<style>
    .header {
        height: 3.5rem;
        padding: 0 .5rem;
        background-color: #343c4a;
    }

    @media (min-width: 992px) {
        .header { padding: 0 1rem; }
    }
</style>