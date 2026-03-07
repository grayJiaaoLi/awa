# Development Objectives

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