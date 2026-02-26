<script>
    import { versions } from "$lib/config.js";
    const version = versions.find((v) => v.id === "v2");

    // State for the AI assistant panel
    // Using simple state without runes for broader compatibility if needed,
    // but since this is Svelte 5, $state() is idiomatic.
    let isExpanded = $state(false);

    function toggleAssistant() {
        isExpanded = !isExpanded;
    }
</script>

<svelte:head>
    <title>{version?.title || "Version 2"} - Academic Writing Assistant</title>
</svelte:head>

<div class="workspace-v2">
    <!-- Writing Area: Full Page -->
    <div class="writing-area">
        <textarea
            placeholder="Start writing your academic paper here..."
            spellcheck="false"
        ></textarea>
    </div>

    <!-- Floating AI Assistant -->
    <!-- svelte-ignore a11y_click_events_have_key_events -->
    <!-- svelte-ignore a11y_no_static_element_interactions -->
    <div class="ai-assistant-wrapper" class:expanded={isExpanded}>
        {#if !isExpanded}
            <button
                class="floating-btn"
                onclick={toggleAssistant}
                aria-label="Open AI Assistant"
            >
                AI
            </button>
        {:else}
            <div class="assistant-panel">
                <div class="panel-header">
                    <h3>AI Assistant</h3>
                    <button
                        class="close-btn"
                        onclick={toggleAssistant}
                        aria-label="Close">×</button
                    >
                </div>

                <div class="chat-output">
                    <div class="message system">
                        <p>
                            I'm here to help. Click the button to collapse me.
                        </p>
                    </div>
                </div>

                <div class="chat-input-area">
                    <input type="text" placeholder="Ask for suggestions..." />
                    <button class="send-btn" aria-label="Send message">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            viewBox="0 0 24 24"
                            fill="currentColor"
                            width="16"
                            height="16"
                        >
                            <path
                                d="M1.946 9.315c-.522-.174-.527-.455.01-.634l19.087-6.362c.529-.176.832.12.684.638l-5.454 19.086c-.15.529-.455.547-.679.045L12 14l6-8-8 6-8.054-2.685z"
                            ></path>
                        </svg>
                    </button>
                </div>
            </div>
        {/if}
    </div>
</div>

<style>
    /* 
        Layout Strategy:
        Writing area fills the viewport.
        Assistant is positioned fixed/absolute relative to viewport or container.
    */
    .workspace-v2 {
        position: relative;
        height: calc(100vh - 220px); /* Fill available space */
        min-height: 500px;
        background-color: white;
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        overflow: hidden; /* Contain the textarea */
    }

    .writing-area {
        height: 100%;
        width: 100%;
        padding-right: 80px; /* Safe area for floating button */
        padding-bottom: 80px; /* Safe area for floating button */
        display: flex;
        flex-direction: column;
    }

    textarea {
        flex: 1;
        width: 100%;
        padding: 3rem; /* Generous padding for clean feel */
        border: none;
        resize: none;
        outline: none;
        font-family: "Cambria", "Georgia", serif;
        font-size: 1.125rem;
        line-height: 1.8;
        color: #1f2937;
    }

    textarea::placeholder {
        color: #9ca3af;
    }

    /* --- Floating Assistant --- */
    .ai-assistant-wrapper {
        position: absolute;
        bottom: 2rem;
        right: 2rem;
        z-index: 10;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* Collapsed State: Button */
    .floating-btn {
        width: 56px;
        height: 56px;
        border-radius: 50%;
        background-color: #3b82f6;
        color: white;
        font-weight: 700;
        font-size: 1.125rem;
        border: none;
        cursor: pointer;
        box-shadow:
            0 4px 6px -1px rgba(0, 0, 0, 0.1),
            0 2px 4px -1px rgba(0, 0, 0, 0.06);
        display: flex;
        align-items: center;
        justify-content: center;
        transition:
            transform 0.2s,
            background-color 0.2s;
    }

    .floating-btn:hover {
        transform: scale(1.05);
        background-color: #2563eb;
    }

    /* Expanded State: Panel */
    .ai-assistant-wrapper.expanded {
        /* Anchored bottom right, but expands */
        width: min(420px, 90vw); /* Responsive max width */
        height: min(500px, 60vh); /* Responsive max height */
    }

    .assistant-panel {
        width: 100%;
        height: 100%;
        background-color: white;
        border: 1px solid #e5e7eb;
        border-radius: 1rem;
        box-shadow:
            0 20px 25px -5px rgba(0, 0, 0, 0.1),
            0 10px 10px -5px rgba(0, 0, 0, 0.04);
        display: flex;
        flex-direction: column;
        overflow: hidden;
        animation: expand 0.25s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    @keyframes expand {
        from {
            opacity: 0;
            transform: scale(0.9) translateY(10px);
        }
        to {
            opacity: 1;
            transform: scale(1) translateY(0);
        }
    }

    .panel-header {
        padding: 0.75rem 1rem;
        border-bottom: 1px solid #f3f4f6;
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #f9fafb;
    }

    .panel-header h3 {
        margin: 0;
        font-size: 1rem;
        font-weight: 600;
        color: #111827;
    }

    .close-btn {
        background: none;
        border: none;
        font-size: 1.5rem;
        color: #6b7280;
        cursor: pointer;
        padding: 0;
        line-height: 1;
        width: 24px;
        height: 24px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        transition: background 0.1s;
    }

    .close-btn:hover {
        background-color: #e5e7eb;
        color: #111827;
    }

    .chat-output {
        flex: 1;
        padding: 1rem;
        overflow-y: auto;
        display: flex;
        flex-direction: column;
        gap: 0.75rem;
    }

    .message {
        padding: 0.75rem;
        border-radius: 0.5rem;
        font-size: 0.875rem;
        line-height: 1.4;
        max-width: 85%;
    }

    .message.system {
        align-self: flex-start;
        background-color: #eff6ff;
        color: #1e40af;
    }

    .chat-input-area {
        padding: 0.75rem;
        border-top: 1px solid #e5e7eb;
        display: flex;
        gap: 0.5rem;
    }

    .chat-input-area input {
        flex: 1;
        padding: 0.5rem 0.75rem;
        border: 1px solid #d1d5db;
        border-radius: 0.375rem;
        font-size: 0.875rem;
        outline: none;
    }

    .chat-input-area input:focus {
        border-color: #3b82f6;
        box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.1);
    }

    .send-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #3b82f6;
        color: white;
        border: none;
        border-radius: 0.375rem;
        padding: 0 0.75rem;
        cursor: pointer;
        transition: background-color 0.15s;
    }

    .send-btn:hover {
        background-color: #2563eb;
    }
</style>
