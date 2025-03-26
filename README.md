# mypackage

A toolkit for publishing.

## Installation

```bash
uv pip install mypackage
```

## Development

This project uses uv for dependency management.

```bash
# Clone the repository
git clone https://github.com/yourusername/mypackage.git
cd mypackage

# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"

# Run tests
pytest

# Format code
black .
isort .

# Type check
mypy src/mypackage

# Generate requirements.txt
uv pip freeze > requirements.txt

# Install from requirements.txt
uv pip install -r requirements.txt
```

## License

MIT 