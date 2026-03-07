# Development Objectives

## 0. (Ground Rules)

* This project is for the demo purpose only.
* When developing, we should implement without over-engineering, and do NOT introduce too much unnecessary complexities in the code.
* The code should be clean, modular, reusable, extendable and efficient.
* The changes and new features should be well-documented, well-tested, and well-maintained.

## 1. (DONE) A running demo page for academic writing with AI-powered assistant.

* Four different versions of the AI assistant UI, allowing users to explore different functionalities and designs.

### 2. (DONE) Use the Third Version as the base to develop a light-weight front- and back-end application for academic writing with AI-powered assistant.

* **Interactive Chatbox UI (Frontend - Version 3):** 
    - An expandable chat interface built with Svelte that tracks conversation history, displays loading indicators, and dynamically renders AI responses in a user-friendly format.
* **Modular FastAPI Backend Service:**
    - A lightweight Python/FastAPI server running at `/api/chat` that securely handles CORS communication with the local frontend and processes AI completions.
* **DeepSeek API Integration:**
    - A plug-and-play AI provider structure currently implementing the DeepSeek `deepseek-chat` model, architected to allow easy addition of other OpenAI-compatible LLMs in the future.

## 3. (DONE) Use the same backend service across all other versions

* **Implement the same backend service across all other versions**
    - Re-used the modular FastAPI service developed in Step 2 across all versions.
    - Verified identical API structures (`/api/chat`) and prompt/provider architecture.
    - Resolved CORS/OPTIONS preflight configuration in `backend/main.py` allowing all origins `["*"]` to ensure compatibility across dynamic Vite server ports (`localhost:5173` / `127.0.0.1:5173`).
* **Achievement of Interactive Chatbox UI across all versions**
    - Replicated the Svelte 5 `$state` engine (`messages`, `inputValue`, `isLoading`) natively into the `v1` and `v2` persistent/floating sidebars.
    - Replicated the AI invocation logic natively into `v4`'s distraction-free inline editor, adapting responses to append as new lines rather than sidebar chat bubbles.

### Developer & Maintenance Notes
- **State Management**: Each version manages its chat history bounds natively using Svelte 5 runes (`$state` and `$effect`). When updating UI component structures, ensure `chatHistoryContainer.scrollTop` logic persists to maintain auto-scrolling capabilities.
- **Provider Architecture**: The backend uses a plug-and-play factory (`get_ai_provider`). Currently, only `DeepSeekProvider` is mapped. When adding a new provider (e.g., Anthropic, OpenAI), extend `AIProvider`, add it into the `get_ai_provider` routing, and verify it uses standard Pydantic models for interactions.
- **CORS Behavior**: A dedicated `@app.options("/api/chat")` override is in place to bypass strict FastAPI preflight restrictions during local Svelte development. If taking this to production, `allow_origins` mapped in `main.py` should be clamped down strictly to the production frontend URL.

## 4. (DONE) Use the Third Version as the base to develop a UI component for writing assignment display

- **Implement a re-useable UI component for writing assignment display**
    - The testing writing task is provided in a text file `writing_assignment.txt`.
    - This component will be shown on the top of the writing canvas field with the same width of writing filed.
    - Inside this component, at the bottom middle position, there should be a responsive button to allow user to expand and collapse it.
    - The UI component should display the writing task in a user-friendly format.
    - The UI component should be re-useable and will be later implemented for across all versions.

### Developer & Maintenance Notes
- **Extracted Text Module**: The assignment text is decoupled into `src/lib/assignmentText.js` as a raw string export. When the text needs to change or if it eventually pulls from a database, update or replace this module. Avoid embedding large raw text directly in Svelte components.
- **Component Layout & State**: The `WritingAssignment.svelte` component manages its own `isExpanded` state using Svelte 5 runes (`$state`). It enforces max-height constraints and uses CSS transitions for smooth expanding/collapsing. It is styled with `position: relative` to maintain the text fog gradients cleanly.
- **Component Reusability**: The component is fully isolated within `src/lib/components/`. It can be plugged across `/v1`, `/v2`, and `/v4` implementations simply by dropping `<WritingAssignment />` above their respective text areas inside their layouts.