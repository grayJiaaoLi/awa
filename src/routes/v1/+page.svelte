<script>
    import { versions } from "$lib/config.js";
    const version = versions.find((v) => v.id === "v1");

    // Chat state
    let messages = $state([
        {
            role: "assistant",
            content:
                "Welcome to Version 1. I am your AI assistant. Type below to ask for suggestions.",
        },
    ]);
    let inputValue = $state("");
    let isLoading = $state(false);
    let chatHistoryContainer = $state(null);

    // Auto-scroll chat history when messages change
    $effect(() => {
        if (messages.length && chatHistoryContainer) {
            chatHistoryContainer.scrollTop = chatHistoryContainer.scrollHeight;
        }
    });

    async function sendMessage() {
        const text = inputValue.trim();
        if (!text || isLoading) return;

        // Add user message to history
        messages = [...messages, { role: "user", content: text }];
        inputValue = "";
        isLoading = true;

        try {
            // Fake delay to simulate network request
            await new Promise(resolve => setTimeout(resolve, 1000));
            
            const dummyResponse = "This is a simulated AI response. Since this is a static demo, there is no real backend connection.";
            messages = [
                ...messages,
                { role: "assistant", content: dummyResponse },
            ];
        } catch (error) {
            console.error("Failed to get AI response:", error);
            messages = [
                ...messages,
                {
                    role: "assistant",
                    content:
                        "Sorry, I encountered an error. Is the backend running?",
                },
            ];
        } finally {
            isLoading = false;
        }
    }
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
        <div class="chat-output" bind:this={chatHistoryContainer}>
            {#each messages as msg}
                <div class="message-wrapper {msg.role}">
                    <div
                        class="message {msg.role === 'assistant'
                            ? 'system'
                            : 'user'}"
                    >
                        <p>{msg.content}</p>
                    </div>
                </div>
            {/each}
            {#if isLoading}
                <div class="message-wrapper assistant">
                    <div class="message system typing">
                        <span class="dot"></span>
                        <span class="dot"></span>
                        <span class="dot"></span>
                    </div>
                </div>
            {/if}
        </div>

        <div class="chat-input-area">
            <input
                type="text"
                placeholder="Ask for suggestions..."
                bind:value={inputValue}
                onkeydown={(e) => {
                    if (e.key === "Enter") {
                        e.preventDefault();
                        sendMessage();
                    }
                }}
            />
            <button
                aria-label="Send message"
                onclick={sendMessage}
                disabled={isLoading}
            >
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
        gap: 0.75rem;
    }

    .message-wrapper {
        display: flex;
        width: 100%;
    }

    .message-wrapper.user {
        justify-content: flex-end;
    }

    .message-wrapper.assistant {
        justify-content: flex-start;
    }

    .message {
        padding: 0.75rem;
        border-radius: 0.5rem;
        font-size: 0.875rem;
        line-height: 1.5;
        max-width: 85%;
        word-wrap: break-word;
    }

    .message.system {
        background-color: #eff6ff;
        color: #1e40af;
        border: 1px solid #dbeafe;
        border-bottom-left-radius: 0.125rem;
    }

    .message.user {
        background-color: #3b82f6;
        color: white;
        border-bottom-right-radius: 0.125rem;
    }

    .message p {
        margin: 0;
        white-space: pre-wrap;
    }

    .message.typing {
        display: flex;
        align-items: center;
        gap: 0.25rem;
        height: 24px;
        padding: 0.5rem 1rem;
    }

    .typing .dot {
        width: 6px;
        height: 6px;
        background-color: #3b82f6;
        border-radius: 50%;
        animation: bounce 1.4s infinite ease-in-out both;
    }

    .typing .dot:nth-child(1) {
        animation-delay: -0.32s;
    }
    .typing .dot:nth-child(2) {
        animation-delay: -0.16s;
    }

    @keyframes bounce {
        0%,
        80%,
        100% {
            transform: scale(0);
        }
        40% {
            transform: scale(1);
        }
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

    button:hover:not(:disabled) {
        background-color: #2563eb;
    }

    button:disabled {
        background-color: #9ca3af;
        cursor: not-allowed;
    }
</style>
