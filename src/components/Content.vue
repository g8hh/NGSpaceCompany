<template>
    <div class="content">
        <div class="container">
            <slot />
        </div>
    </div>
</template>

<style>
    .content {
        height: calc(100% - 3.5rem);
        padding: 1rem 0;
    }

    .container {
        padding: 0 .5rem;
    }

    @media (min-width: 992px) {
        .container { max-width: 720px; }
    }
</style>
