# List out available commands
default:
	@just --list

# Launch API in debug mode
run:
	@echo "Running main app..."
	uv run python app.py

# Build Docker image
build-docker:
	@echo "Building docker image..."
	docker build -t fizzbuzz-api:latest -f ./Dockerfile .
	@echo "Docker image built successfully!"

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
	@echo "Cleaned out unused files and directories!"

# Run PyTest unit tests
pytest *args:
	@echo "Running unittest suite..."
	poetry run pytest {{ args }}
