# List out available commands
default:
	@just --list

# Install dependencies
install:
	@echo "Installing dependencies..."
	uv sync --all-extras
	npm install

# Build Docker image
build:
	@echo "Building docker images..."
	docker compose build
	@echo "Docker images built successfully!"

# Start Docker containers
start:
	@echo "Starting services in Docker containers..."
	docker compose up

# Shut down Docker containers
stop:
	@echo "Stopping Docker containers..."
	docker compose down

# Launch backend API (development)
run-backend:
	@echo "Running backend API in development mode..."
	uv run python app.py

# Launch frontend (development)
run-frontend:
	@echo "Running frontend in development mode..."
	npm run dev

# View Docker logs
logs:
	@echo "Viewing Docker logs..."
	docker compose logs -f

# Clean unused files
clean:
	-@find ./ -name '*.pyc' -exec rm -f {} \;
	-@find ./ -name '__pycache__' -exec rm -rf {} \;
	-@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	-@find ./ -name '*~' -exec rm -f {} \;
	-@rm -rf .pytest_cache
	-@rm -rf .cache
	-@rm -rf .mypy_cache
	-@rm -rf build
	-@rm -rf dist
	-@rm -rf *.egg-info
	-@rm -rf htmlcov
	-@rm -rf .tox/
	-@rm -rf docs/_build
	-@rm -rf .venv
	-@rm -rf node_modules
	-@rm -rf .next
	@echo "Cleaned out unused files and directories!"

# Run PyTest unit tests (legacy command)
pytest *args:
	@echo "Running unittest suite..."
	pytest {{ args }}
