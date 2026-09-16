client-build-and-run:
	npm run build --prefix ./src/client/frontend/deltanet-client-frontend
	poetry run deltanet-client
