# Academic Writing Assistant (AWA)

Welcome to the **Academic Writing Assistant (AWA)** demo repository. This project showcases a SvelteKit-based web application designed to assist users with their academic writing processes.

## 🚀 Live Demo

Access and play around with the live demo:
**[View Live Demo](https://grayjiaaoli.github.io/awa/)**

The application features four versions of the academic writing assistant UI, allowing users to explore different functionalities and designs.

From the first version to the fourth, the AI assistant's presence gradually diminished while the immersive writing experience progressively deepened.

### Version 1
The writing area is positioned alongside the AI assistant, enabling users to easily access the AI assistant.

### Version 2
The AI assistant is hidden in the lower right corner by default, allowing users to enjoy a relatively immersive writing experience.
When users click on it, it expands into a small window that allows for further interaction.

### Version 3
Similar in intent to Version 2, but employing a design with an input field positioned below the screen. 
This approach provides appropriate guidance or encouragement for users interacting with the AI assistant.

### Version 4
This version requires users to **double-tap the Spacebar** to evoke the AI assistant.
This design hides the AI assistant entirely, delivering an immersive writing experience.


---

## 💻 Development Instructions

This project is structured as a full-stack application with a **SvelteKit** frontend and a **FastAPI (Python)** backend. Follow these steps to set up and run the application locally.

### Prerequisites
- [Node.js](https://nodejs.org/) (version 18+ recommended) and `npm` installed.
- [Python](https://www.python.org/) 3.9+ installed.
- A DeepSeek API key (or another OpenAI-compatible API key) for the backend.

### 1. Installation

Clone the repository:
```sh
git clone https://github.com/grayJiaaoLi/awa.git
cd awa
```

**Frontend Setup:**
Install the SvelteKit dependencies:
```sh
npm install
```

**Backend Setup:**
Navigate to the backend directory, create a virtual environment, and install the necessary Python packages:
```sh
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```
Next, create a `.env` file inside the `backend/` directory and add your DeepSeek API key:
```env
DEEPSEEK_API_KEY=your_actual_api_key_here
```

### 2. Running Locally for Development

You will need to run the frontend and backend in two separate terminal windows.

**Start the FastAPI Backend:**
```sh
# Ensure you are in the awa/backend directory with the venv activated
uvicorn main:app --reload
```
The backend API will be available at `http://127.0.0.1:8000`.

**Start the SvelteKit Frontend:**
```sh
# Ensure you are in the main awa/ directory
npm run dev

# Or start the server and automatically open the app in your default browser:
npm run dev -- --open
```
The app will be available at `http://localhost:5173`.

### 4. Deployment

This repository uses `@sveltejs/adapter-static` and is configured to automatically deploy to GitHub Pages anytime changes are pushed to the `main` branch. This is handled by the GitHub Actions workflow located in `.github/workflows/deploy.yml`.
