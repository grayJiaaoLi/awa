<script>
    import { versions } from "$lib/config.js";
    import { onMount } from "svelte";

    const version = versions.find((v) => v.id === "v4");

    // Each line is an object with unique ID and content
    let lines = $state([{ id: crypto.randomUUID(), text: "", showAi: false }]);

    // Active line index for highlighting
    let activeLineIndex = $state(0);

    /** @param {number} index */
    function setActive(index) {
        activeLineIndex = index;
    }

    /** @param {KeyboardEvent} event, @param {number} index */
    function handleKeydown(event, index) {
        if (event.key === "Enter") {
            event.preventDefault();
            const newLine = {
                id: crypto.randomUUID(),
                text: "",
                showAi: false,
            };
            lines.splice(index + 1, 0, newLine);
            activeLineIndex = index + 1;
            setTimeout(() => focusLine(activeLineIndex), 0);
        } else if (
            event.key === "Backspace" &&
            lines[index].text === "" &&
            lines.length > 1
        ) {
            event.preventDefault();
            lines.splice(index, 1);
            activeLineIndex = Math.max(0, index - 1);
            setTimeout(() => focusLine(activeLineIndex, true), 0);
        } else if (event.key === "ArrowUp" && index > 0) {
            event.preventDefault();
            activeLineIndex = index - 1;
            focusLine(activeLineIndex);
        } else if (event.key === "ArrowDown" && index < lines.length - 1) {
            event.preventDefault();
            activeLineIndex = index + 1;
            focusLine(activeLineIndex);
        } else if (event.key === "Escape") {
            lines[index].showAi = false;
        }
    }

    /** @param {Event} event, @param {number} index */
    function handleInput(event, index) {
        // @ts-ignore
        const value = event.target.value;
        const previousValue = lines[index].text;
        lines[index].text = value;

        if (value.endsWith("  ") && !previousValue.endsWith("  ")) {
            // Remove the two spaces
            const trimmedValue = value.slice(0, -2);
            lines[index].text = trimmedValue;
            // Update the input element value immediately to reflect the trim
            // @ts-ignore
            event.target.value = trimmedValue;

            showAiComposer(index);
        }
    }

    /** @param {number} index */
    function showAiComposer(index) {
        // Close others first
        lines.forEach((l) => (l.showAi = false));
        lines[index].showAi = true;
    }

    /** @param {number} index */
    function focusLine(index, atEnd = false) {
        const el = document.getElementById(`line-${index}`);
        if (el) {
            el.focus();
            if (atEnd) {
                // @ts-ignore
                el.setSelectionRange(el.value.length, el.value.length);
            }
        }
    }

    /** @param {number} index */
    function closeAi(index) {
        if (lines[index]) {
            lines[index].showAi = false;
            focusLine(index);
        }
    }

    /** @param {MouseEvent} event */
    function handleWindowClick(event) {
        // Close all composers if clicking outside
        // We use a specific class to stop propagation on the composer itself
        // @ts-ignore
        const target = /** @type {HTMLElement} */ (event.target);
        if (!target.closest(".ai-composer") && !target.closest(".line-input")) {
            lines.forEach((l) => (l.showAi = false));
        }
    }
</script>

<svelte:head>
    <title>{version?.title || "Version 4"} - Academic Writing Assistant</title>
</svelte:head>

<svelte:window onclick={handleWindowClick} />

<div class="workspace-v4">
    <div class="editor-container">
        {#each lines as line, i (line.id)}
            <div class="line-wrapper">
                <div
                    class="gutter"
                    class:has-content={line.text.trim().length > 0}
                    class:active={i === activeLineIndex}
                >
                    {i + 1}
                </div>

                <div class="line-content">
                    <input
                        id="line-{i}"
                        type="text"
                        class="line-input"
                        value={line.text}
                        oninput={(e) => handleInput(e, i)}
                        onkeydown={(e) => handleKeydown(e, i)}
                        onfocus={() => setActive(i)}
                        placeholder={(line.text === "" &&
                            i === lines.length - 1) ||
                        (line.text === "" && i === activeLineIndex)
                            ? "Press Space Twice for AI"
                            : ""}
                        autocomplete="off"
                    />

                    {#if line.showAi}
                        <div class="ai-composer-wrapper">
                            <div class="ai-composer">
                                <input
                                    type="text"
                                    placeholder="Ask AI to continue writing..."
                                    onkeydown={(e) =>
                                        e.key === "Escape" && closeAi(i)}
                                />
                                <button
                                    class="send-btn"
                                    onclick={() => closeAi(i)}
                                >
                                    <span class="arrow">↑</span>
                                </button>
                            </div>
                        </div>
                    {/if}
                </div>
            </div>
        {/each}

        <!-- svelte-ignore a11y_click_events_have_key_events -->
        <!-- svelte-ignore a11y_no_static_element_interactions -->
        <div
            class="bottom-area"
            onclick={() => focusLine(lines.length - 1, true)}
        ></div>
    </div>
</div>

<style>
    .workspace-v4 {
        height: calc(100vh - 220px);
        min-height: 500px;
        background-color: white;
        border: 1px solid #e5e7eb;
        border-radius: 0.5rem;
        display: flex;
        flex-direction: column;
        overflow: hidden;
    }

    .editor-container {
        flex: 1;
        overflow-y: auto;
        padding: 2rem 0;
        display: flex;
        flex-direction: column;
    }

    .line-wrapper {
        display: flex;
        width: 100%;
        position: relative;
    }

    .gutter {
        width: 60px;
        min-width: 60px;
        text-align: right;
        padding-right: 1.5rem;
        color: #e5e7eb;
        font-family: monospace;
        font-size: 0.875rem;
        user-select: none;
        padding-top: 0.5rem;
    }

    .gutter.has-content {
        color: #374151;
    }

    .gutter.active {
        color: #9ca3af;
        font-weight: bold;
    }

    .line-content {
        flex: 1;
        padding-right: 2rem;
        display: flex;
        flex-direction: column;
        position: relative; /* Anchor for absolute composer */
    }

    .line-input {
        width: 100%;
        border: none;
        outline: none;
        font-family: "Georgia", serif;
        font-size: 1.125rem;
        padding: 0.25rem 0;
        color: #1f2937;
        background: transparent;
        z-index: 1; /* Keep text interactive */
    }

    .line-input::placeholder {
        color: #d1d5db;
        font-style: italic;
        font-size: 0.95rem;
    }

    .ai-composer-wrapper {
        position: absolute;
        top: 100%; /* Float directly below the input line */
        left: 0;
        width: 100%;
        max-width: 600px;
        z-index: 50; /* Ensure it floats above subsequent lines */
        padding-top: 0.25rem;
        pointer-events: none; /* Let clicks pass through wrapper areas if needed */
    }

    .ai-composer {
        background-color: white;
        border: 1px solid #e5e7eb;
        border-radius: 2rem;
        padding: 0.25rem 0.5rem 0.25rem 1rem;
        display: flex;
        align-items: center;
        box-shadow:
            0 10px 15px -3px rgba(0, 0, 0, 0.1),
            0 4px 6px -2px rgba(0, 0, 0, 0.05);
        pointer-events: auto; /* Re-enable for the actual box */
        animation: slideDown 0.15s ease-out;
    }

    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-5px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .ai-composer input {
        flex: 1;
        border: none;
        background: transparent;
        outline: none;
        padding: 0.5rem;
        font-size: 0.95rem;
        color: #374151;
        min-width: 0;
    }

    .send-btn {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        background-color: #111827;
        color: white;
        border: none;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: transform 0.1s;
        flex-shrink: 0;
    }

    .send-btn:hover {
        transform: scale(1.05);
    }

    .arrow {
        font-size: 1.1rem;
        line-height: 1;
    }

    .bottom-area {
        flex: 1;
        min-height: 2rem;
        cursor: text;
    }
</style>
