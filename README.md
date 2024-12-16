<div align="center">
<img src=".https://github.com/YanickJair/catface/blob/main/assets/catface-logo.svg" width="200" height="200" alt="Catface Logo">

# Catface
</div>

## Features

- **Documentation (MkDocs)**
  - Automatic API documentation
  - Material design theme
  - Ready-to-deploy structure

- **Docker Integration**
  - Multi-stage builds
  - Production-ready configuration
  - Python version specific base images

- **Development Tools**
  - Pre-commit hooks for code quality
  - Ruff for fast linting and formatting
  - Tox for testing across Python versions

## Quick Start

```bash
# Install Catface
pip install catface

# Create a new project
catface my-awesome-project
```

## Pre-configured Tox file

  - Task automation: Using Tox we can automate repetitive tasks
  - Test against multiple Python versions
  - Environment management: Using Tox we can create different environments each with its dependencies
  - Lint and format code using Ruff

```bash
# Cd inside your project
cd my-awesome-project

tox # runs all environments
tox -e <env_name> # running each environment individually by name
tox -p all # parallel execution
