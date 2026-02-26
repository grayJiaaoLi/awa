<script>
	import "../app.css";
	import { base } from '$app/paths';
</script>

<div class="app-shell">
	<header>
		<div class="container header-content">
			<a href="{base}/" class="brand">Academic Writing Assistant</a>
		</div>
	</header>

	<main class="container">
		<slot />
	</main>
</div>

<style>
	.app-shell {
		min-height: 100vh;
		display: flex;
		flex-direction: column;
	}

	header {
		background-color: white;
		border-bottom: 1px solid #e5e7eb;
		padding: 1rem 0;
		margin-bottom: 2rem;
	}

	.header-content {
		display: flex;
		align-items: center;
	}

	.brand {
		font-weight: 700;
		font-size: 1.25rem;
		color: #111827;
		text-decoration: none;
	}

	main {
		flex: 1;
		width: 100%;
		padding-bottom: 2rem;
	}

	footer {
		background-color: white;
		border-top: 1px solid #e5e7eb;
		padding: 1.5rem 0;
		color: #6b7280;
		font-size: 0.875rem;
		text-align: center;
	}
</style>
