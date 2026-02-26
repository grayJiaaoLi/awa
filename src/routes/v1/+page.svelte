<script>
    import { versions } from "$lib/config.js";
    const version = versions.find((v) => v.id === "v1");
</script>

<svelte:head>
    <title>{version?.title || "Version 1"} - Academic Writing Assistant</title>
</svelte:head>

<div class="workspace">
    <!-- Left Side: Writing Area (75%) -->
    <div class="writing-area">
        <textarea
            placeholder="Start writing your academic paper here..."
            spellcheck="false"
        ></textarea>
    </div>

    <!-- Right Side: AI Assistant Panel (25%) -->
    <div class="assistant-panel">
        <div class="chat-output">
            <div class="message system">
                <p>Welcome to Version 1. I am your AI assistant.</p>
            </div>
            <!-- Future messages will appear here -->
        </div>

        <div class="chat-input-area">
            <input type="text" placeholder="Ask for suggestions..." />
            <button aria-label="Send message">
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
</div>

<style>
    /* 
        Layout Strategy:
        Flex container filling the available height.
        Calculated height accounts for the header/footer in the main layout.
    */
    .workspace {
        display: flex;
        height: calc(
            100vh - 220px
        ); /* Approx height to fill viewport between header/footer */
        min-height: 500px;
        background-color: white;
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        overflow: hidden;
        box-shadow:
            0 1px 3px 0 rgba(0, 0, 0, 0.1),
            0 1px 2px 0 rgba(0, 0, 0, 0.06);
    }

    /* --- Left Section --- */
    .writing-area {
        flex: 3; /* 75% */
        display: flex;
        flex-direction: column;
    }

    textarea {
        flex: 1;
        width: 100%;
        padding: 2rem;
        border: none;
        resize: none;
        outline: none;
        font-family: "Georgia", "Cambria", "Times New Roman", serif; /* Serif for academic feel */
        font-size: 1.125rem;
        line-height: 1.8;
        color: #1f2937;
    }

    textarea::placeholder {
        color: #9ca3af;
    }

    /* --- Right Section --- */
    .assistant-panel {
        flex: 1; /* 25% */
        display: flex;
        flex-direction: column;
        background-color: #f9fafb; /* Slightly tinted/darker */
        border-left: 1px solid #e5e7eb;
    }

    .chat-output {
        flex: 1;
        padding: 1rem;
        overflow-y: auto;
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }

    .message {
        padding: 0.75rem;
        border-radius: 0.5rem;
        font-size: 0.875rem;
        line-height: 1.5;
    }

    .message.system {
        background-color: #eff6ff;
        color: #1e40af;
        border: 1px solid #dbeafe;
    }

    .message p {
        margin: 0;
    }

    .chat-input-area {
        padding: 0.75rem;
        background-color: white;
        border-top: 1px solid #e5e7eb;
        display: flex;
        gap: 0.5rem;
    }

    input {
        flex: 1;
        padding: 0.5rem 0.75rem;
        border: 1px solid #d1d5db;
        border-radius: 0.375rem;
        font-size: 0.875rem;
        outline: none;
        transition: border-color 0.15s;
    }

    input:focus {
        border-color: #3b82f6;
        box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.1);
    }

    button {
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

    button:hover {
        background-color: #2563eb;
    }
</style>
