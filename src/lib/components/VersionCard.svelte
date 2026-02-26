<script>
    import { base } from "$app/paths";
    /** @type {{ version: import('../config.js').Version }} */
    let { version } = $props();
</script>

<a href="{base}{version.href}" class="version-card">
    {#if version.image}
        <img
            src="{base}{version.image}"
            alt="{version.title} Preview"
            class="preview-image"
        />
    {:else}
        <div class="image-placeholder">
            <span>Preview Placeholder</span>
        </div>
    {/if}
    <div class="content">
        <h2>{version.title}</h2>
        <p>{version.description}</p>
        <div class="arrow">→</div>
    </div>
</a>

<style>
    .version-card {
        display: flex;
        flex-direction: column;
        border: 1px solid #e5e7eb;
        border-radius: 0.75rem;
        text-decoration: none;
        color: inherit;
        background-color: white;
        transition: all 0.2s ease;
        height: 100%;
        overflow: hidden; /* Ensure image doesn't overflow corners */
    }

    .version-card:hover {
        transform: translateY(-2px);
        box-shadow:
            0 10px 15px -3px rgba(0, 0, 0, 0.1),
            0 4px 6px -2px rgba(0, 0, 0, 0.05);
        border-color: #3b82f6;
    }

    .image-placeholder {
        height: 200px;
        background-color: #f3f4f6;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #9ca3af;
        font-size: 0.875rem;
        font-weight: 500;
        border-bottom: 1px solid #e5e7eb;
    }

    .preview-image {
        width: 100%;
        height: 200px;
        object-fit: contain;
        border-bottom: 1px solid #e5e7eb;
    }

    .content {
        padding: 1.5rem;
        display: flex;
        flex-direction: column;
        flex-grow: 1;
    }

    h2 {
        font-size: 1.25rem;
        font-weight: 600;
        margin: 0 0 0.5rem 0;
        color: #111827;
    }

    .arrow {
        align-self: flex-end;
        font-weight: bold;
        color: #3b82f6;
        margin-top: 1rem;
    }

    p {
        font-size: 0.875rem;
        color: #6b7280;
        margin: 0;
        line-height: 1.5;
        flex-grow: 1;
    }
</style>
