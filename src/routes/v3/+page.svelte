<script>
    import { versions } from "$lib/config.js";
    const version = versions.find((v) => v.id === "v3");

    // State for the inline assistant
    let isExpanded = $state(false);
    let assistantContainer;

    function expand() {
        isExpanded = true;
    }

    function collapse() {
        isExpanded = false;
    }

    /** @param {MouseEvent} event */
    function handleWindowClick(event) {
        // If click is outside the assistant container, collapse it
        if (
            isExpanded &&
            assistantContainer &&
            !assistantContainer.contains(event.target)
        ) {
            collapse();
        }
    }

    /** @param {KeyboardEvent} event */
    function handleKeydown(event) {
        if (event.key === "Escape" && isExpanded) {
            collapse();
        }
    }
</script>

<svelte:head>
    <title>{version?.title || "Version 3"} - Academic Writing Assistant</title>
</svelte:head>

<svelte:window onclick={handleWindowClick} onkeydown={handleKeydown} />

<div class="workspace-v3">
    <!-- Writing Area (Top) -->
    <div class="writing-area">
        <textarea
            placeholder="Start writing your academic paper here..."
            spellcheck="false"
        ></textarea>
    </div>

    <!-- Assistant Area (Bottom) -->
    <div
        class="assistant-area"
        class:expanded={isExpanded}
        bind:this={assistantContainer}
    >
        {#if isExpanded}
            <!-- Expanded: History + Input -->
            <div class="chat-history">
                <div class="message system">
                    <p>Assistant ready. Type below to ask for help.</p>
                </div>
            </div>
        {/if}

        <!-- Input Row (Always visible, expands panel on focus/click) -->
        <div
            class="input-row"
            role="button"
            tabindex="0"
            onclick={expand}
            onkeydown={(e) => {
                if (e.key === "Enter" || e.key === " ") expand();
            }}
        >
            <input
                type="text"
                placeholder="Ask the assistant..."
                onfocus={expand}
            />
            <button class="send-btn" aria-label="Send">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="currentColor"
                    width="16"
                    height="16"
                >
                    <path
                        d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"
                        transform="rotate(-90 12 12)"
                    ></path>
                </svg>
            </button>
        </div>
    </div>
</div>

<style>
    .workspace-v3 {
        display: flex;
        flex-direction: column;
        height: calc(100vh - 220px);
        min-height: 500px;
        background-color: white;
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        overflow: hidden;
        position: relative;
    }

    .writing-area {
        flex: 1;
        display: flex;
        flex-direction: column;
        overflow: hidden;
    }

    textarea {
        flex: 1;
        width: 100%;
        padding: 3rem;
        border: none;
        resize: none;
        outline: none;
        font-family: "Georgia", serif;
        font-size: 1.125rem;
        line-height: 1.8;
        color: #1f2937;
    }

    textarea::placeholder {
        color: #9ca3af;
    }

    /* --- Assistant Area --- */
    .assistant-area {
        /* Centered and 80% width as requested */
        width: 80%;
        margin: 0 auto 2rem auto; /* Margin from bottom */
        background-color: white;
        border: 1px solid #e5e7eb;
        border-radius: 0.75rem;
        box-shadow:
            0 4px 6px -1px rgba(0, 0, 0, 0.1),
            0 2px 4px -1px rgba(0, 0, 0, 0.06);
        transition:
            height 0.3s cubic-bezier(0.16, 1, 0.3, 1),
            box-shadow 0.3s ease;
        display: flex;
        flex-direction: column;
        overflow: hidden;
        z-index: 10;

        /* Height transition logic */
        height: 50px; /* Collapsed height approx */
    }

    .assistant-area.expanded {
        height: 25vh; /* Expanded height */
        box-shadow:
            0 10px 15px -3px rgba(0, 0, 0, 0.1),
            0 4px 6px -2px rgba(0, 0, 0, 0.05);
        border-color: #3b82f6;
    }

    .chat-history {
        flex: 1;
        padding: 1rem;
        overflow-y: auto;
        background-color: #f9fafb;
        border-bottom: 1px solid #f3f4f6;
    }

    .message {
        padding: 0.5rem 0.75rem;
        border-radius: 0.5rem;
        font-size: 0.875rem;
        color: #4b5563;
        background-color: #e5e7eb;
        display: inline-block;
    }

    .input-row {
        display: flex;
        align-items: center;
        padding: 0.5rem;
        background-color: white;
        height: 50px; /* Matches collapsed height */
    }

    input {
        flex: 1;
        border: none;
        outline: none;
        padding: 0 1rem;
        font-size: 0.95rem;
        color: #374151;
        height: 100%;
        background: transparent;
    }

    input::placeholder {
        color: #9ca3af;
    }

    .send-btn {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        background-color: #3b82f6;
        color: white;
        border: none;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: background-color 0.2s;
        margin-right: 0.25rem;
    }

    .send-btn:hover {
        background-color: #2563eb;
    }
</style>
