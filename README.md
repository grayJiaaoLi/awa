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

This project is built using [SvelteKit](https://kit.svelte.dev/). Follow these steps to run the application locally for development or testing:

### Prerequisites
Make sure you have [Node.js](https://nodejs.org/) (version 18+ recommended) and `npm` installed on your machine.

### 1. Installation

Clone the repository and install the dependencies:
```sh
git clone https://github.com/grayJiaaoLi/awa.git
cd awa
npm install
```

### 2. Running Locally

Start the local development server:
```sh
npm run dev

# Or start the server and automatically open the app in your default browser:
npm run dev -- --open
```
The app will typically be available at `http://localhost:5173`.

### 3. Building for Production

To create a production-ready static build of the application:
```sh
npm run build
```
The static files will be generated in the `build/` directory. You can preview this production build locally before deployment using:
```sh
npm run preview
```

### 4. Deployment

This repository uses `@sveltejs/adapter-static` and is configured to automatically deploy to GitHub Pages anytime changes are pushed to the `main` branch. This is handled by the GitHub Actions workflow located in `.github/workflows/deploy.yml`.
