<script>
    import { versions } from "$lib/config.js";
    import VersionCard from "$lib/components/VersionCard.svelte";
</script>

<svelte:head>
    <title>Academic Writing Assistant</title>
</svelte:head>

<div class="grid">
    {#each versions as version}
        <VersionCard {version} />
    {/each}
</div>

<style>
    .grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 2rem;
        padding-bottom: 2rem;
        max-width: 900px;
        margin: 0 auto;
    }

    /* Responsive adjustments: stack on small screens */
    @media (max-width: 640px) {
        .grid {
            grid-template-columns: 1fr;
        }
    }
</style>
