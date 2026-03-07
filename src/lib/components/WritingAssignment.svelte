<script>
    import { assignmentText } from "$lib/assignmentText.js";

    let isExpanded = $state(false);

    function toggleExpand() {
        isExpanded = !isExpanded;
    }
</script>

<div class="assignment-wrapper">
    <div class="assignment-container" class:expanded={isExpanded}>
        <div class="assignment-header">
            <h3>Writing Assignment</h3>
        </div>

        <div class="assignment-content">
            {#each assignmentText.split("\n") as paragraph}
                {#if paragraph.trim() !== ""}
                    <p>{paragraph}</p>
                {/if}
            {/each}
        </div>

        {#if !isExpanded}
            <div class="fog"></div>
        {/if}
    </div>

    <div class="button-container">
        <button
            class="toggle-btn"
            onclick={toggleExpand}
            aria-label="Toggle Writing Assignment"
        >
            <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="chevron-icon"
            >
                {#if isExpanded}
                    <polyline points="18 15 12 9 6 15"></polyline>
                {:else}
                    <polyline points="6 9 12 15 18 9"></polyline>
                {/if}
            </svg>
        </button>
    </div>
</div>

<style>
    .assignment-wrapper {
        display: flex;
        flex-direction: column;
        border-bottom: 1px solid #e5e7eb;
        background-color: #fafafa;
        position: relative;
    }

    .assignment-container {
        position: relative;
        max-height: 120px; /* Collapsed height */
        overflow: hidden;
        transition: max-height 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .assignment-container.expanded {
        max-height: 800px;
        overflow-y: auto;
    }

    .assignment-header {
        padding: 1.5rem 3rem 0.5rem 3rem;
    }

    .assignment-header h3 {
        margin: 0;
        font-size: 0.875rem;
        color: #6b7280;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .assignment-content {
        padding: 0 3rem 2rem 3rem;
        color: #374151;
        font-family: "Georgia", serif;
        font-size: 1.05rem;
        line-height: 1.6;
    }

    .assignment-content p {
        margin-top: 0;
        margin-bottom: 1rem;
    }

    .assignment-content p:last-child {
        margin-bottom: 0;
    }

    .fog {
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 60px;
        background: linear-gradient(
            to bottom,
            rgba(250, 250, 250, 0),
            rgba(250, 250, 250, 1)
        );
        pointer-events: none;
    }

    .button-container {
        display: flex;
        justify-content: center;
        margin-top: -16px;
        z-index: 10;
        position: relative;
        padding-bottom: 0.5rem;
    }

    .toggle-btn {
        width: 48px;
        height: 24px;
        background-color: white;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        color: #6b7280;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
        transition: all 0.2s;
    }

    .toggle-btn:hover {
        background-color: #f9fafb;
        color: #374151;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .chevron-icon {
        width: 16px;
        height: 16px;
    }
</style>
