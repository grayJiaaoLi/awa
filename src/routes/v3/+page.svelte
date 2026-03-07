<script>
    import { versions } from "$lib/config.js";
    import WritingAssignment from "$lib/components/WritingAssignment.svelte";
    const version = versions.find((v) => v.id === "v3");

    // State for the inline assistant
    let isExpanded = $state(false);
    let assistantContainer;

    // Chat state
    let messages = $state([
        {
            role: "assistant",
            content: "Assistant ready. Type below to ask for help.",
        },
    ]);
    let inputValue = $state("");
    let isLoading = $state(false);
    let chatHistoryContainer = $state(null);

    function expand() {
        isExpanded = true;
    }

    function collapse() {
        isExpanded = false;
    }

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
        expand();

        try {
            // Send exactly the format the backend expects
            const response = await fetch("http://localhost:8000/api/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    messages: messages.map((m) => ({
                        role: m.role,
                        content: m.content,
                    })),
                    provider: "deepseek",
                }),
            });

            if (!response.ok) {
                throw new Error(`Error: ${response.status}`);
            }

            const data = await response.json();
            messages = [
                ...messages,
                { role: "assistant", content: data.response },
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
        <WritingAssignment />
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
            <div class="chat-history" bind:this={chatHistoryContainer}>
                {#each messages as msg}
                    <div class="message-wrapper {msg.role}">
                        <div class="message {msg.role}">
                            <p>{msg.content}</p>
                        </div>
                    </div>
                {/each}
                {#if isLoading}
                    <div class="message-wrapper assistant">
                        <div class="message assistant typing">
                            <span class="dot"></span>
                            <span class="dot"></span>
                            <span class="dot"></span>
                        </div>
                    </div>
                {/if}
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
                bind:value={inputValue}
                onfocus={expand}
                onkeydown={(e) => {
                    if (e.key === "Enter") {
                        e.stopPropagation();
                        sendMessage();
                    }
                }}
            />
            <button
                class="send-btn"
                aria-label="Send"
                onclick={(e) => {
                    e.stopPropagation();
                    sendMessage();
                }}
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
        padding: 0.5rem 0.75rem;
        border-radius: 0.5rem;
        font-size: 0.875rem;
        line-height: 1.4;
        max-width: 85%;
        word-wrap: break-word;
    }

    .message p {
        margin: 0;
        white-space: pre-wrap;
    }

    .message.user {
        background-color: #3b82f6;
        color: white;
        border-bottom-right-radius: 0.125rem;
    }

    .message.assistant {
        background-color: #e5e7eb;
        color: #1f2937;
        border-bottom-left-radius: 0.125rem;
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
        background-color: #6b7280;
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

    .send-btn:hover:not(:disabled) {
        background-color: #2563eb;
    }

    .send-btn:disabled {
        background-color: #9ca3af;
        cursor: not-allowed;
    }
</style>
