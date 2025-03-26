# My Package 🚀

A sample Python package with modern development practices.

## Quick Start 🏃‍♂️

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mypackage.git
cd mypackage
```

2. Set up your development environment:
```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create a virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
uv pip install -e ".[dev]"
```

## Development Guide 🛠️

### Running Tests 🧪
```bash
pytest
# To see coverage report
pytest --cov
```

### Code Quality Tools 🎯

We use several tools to maintain code quality:

1. **Formatting** (makes code pretty):
```bash
# Check formatting
ruff format . --check

# Fix formatting
ruff format .
```

2. **Linting** (finds potential errors):
```bash
# Check for issues
ruff check .

# Fix auto-fixable issues
ruff check . --fix
```

3. **Type Checking** (ensures correct type usage):
```bash
mypy src/mypackage
```

### Testing GitHub Actions Locally 🔄

We use `act` to test GitHub Actions workflows locally. This helps catch workflow issues before pushing to GitHub.

1. Install `act`:
```bash
# On macOS
brew install act

# On Linux
curl -s https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# On Windows (using Chocolatey)
choco install act-cli
```

2. Run workflows locally:
```bash
# Run all workflows
act

# Run a specific job
act -j quality

# Run with verbose output
act -v

# List all available actions
act -l
```

Note: `act` requires Docker to be installed and running on your system.

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Need Help? 💡

- Create an issue on GitHub
- Check the [project documentation](link-to-docs)
- Reach out to the team

---
Made with ❤️ by Your Team

## GitHub Actions CI/CD 🤖

Every push and pull request triggers our CI pipeline which:
- Runs all tests
- Checks code formatting
- Runs the linter
- Performs type checking

You can see the workflow status in the GitHub Actions tab.

## Common Issues & Solutions 🔧

### Virtual Environment Issues
If you see "command not found" errors:
```bash
# Make sure you've activated the virtual environment
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

### Import Errors
If you see import errors during development:
```bash
# Make sure you've installed the package in editable mode
uv pip install -e ".[dev]"
```

### Cache Issues
If tools aren't working as expected:
```bash
# Try cleaning and reinstalling
rm -rf .venv
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
```

### Act Issues
If you encounter issues with `act`:
```bash
# Make sure Docker is running
docker ps

# Try running with verbose output to debug
act -v

# Use minimal images for faster runs
act -P ubuntu-latest=catthehacker/ubuntu:act-latest
```

## Contributing 🤝

1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes
4. Run all checks:
   ```bash
   pytest
   ruff format . --check
   ruff check .
   mypy src/mypackage
   ```
5. Test GitHub Actions locally with `act`
6. Create a Pull Request 