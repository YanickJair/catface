<h1 align="center">
  <img src="https://raw.githubusercontent.com/YanickJair/catface/main/static/catface-logo.png" alt="catface" width="200px">
  <br>
</h1>

<p align="center">
<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-_red.svg"></a>
</p>

`catface` s a Command Line Interface (CLI) tool that helps you create Python projects with best practices built-in. It uses [cookiecutter](https://www.cookiecutter.io/) under the hood to provide project templates that you can customize based on your needs.


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

<h1 align="center">
  <img src="https://raw.githubusercontent.com/YanickJair/catface/main/static/features-prompt.png" alt="catface" width="700px">
  <br>
</h1>

<h1 align="center">
  <img src="https://raw.githubusercontent.com/YanickJair/catface/main/static/python-version.png" alt="catface" width="700px">
  <br>
</h1>


## Project structure
The final project structure is going to be something like this based on the features you choose.
<h1 align="center">
  <img src="https://raw.githubusercontent.com/YanickJair/catface/main/static/done.png" alt="catface" width="700px">
  <br>
</h1>


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
