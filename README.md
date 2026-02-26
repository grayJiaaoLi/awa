# Academic Writing Assistant (AWA)

Welcome to the **Academic Writing Assistant (AWA)** demo repository. This project showcases a SvelteKit-based web application designed to assist users with their academic writing processes.

## 🚀 Live Demo

You can easily access and play around with the active demo hosted on GitHub Pages:
**[View Live Demo](https://grayjiaaoli.github.io/awa/)**

The application features multiple iterations (or versions) of the writing assistant UI, allowing users to explore different functionalities and design approaches directly from the main landing page.

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
