import os
import subprocess
import sys
from pathlib import Path
import shutil


REMOVE_PATHS = [
    '{% if cookiecutter.packaging != "pip" %} requirements.txt {% endif %}',
    '{% if cookiecutter.packaging != "poetry" %} poetry.lock {% endif %}',
]

project_name = "{{ cookiecutter.project_name }}"
project_description = "{{ cookiecutter.project_description }}"


for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)

def remove_docker_file():
    os.remove('Dockerfile')
    if os.path.exists('docker-compose.yml'):
        os.remove('docker-compose.yml')

def setup_mkdocs():
    """Set up MkDocs documentation."""
    docs_dir = Path('docs')
    docs_dir.mkdir(exist_ok=True)

    # Create initial documentation files
    (docs_dir / 'index.md').write_text(f'# {project_name}\n\n{project_description}')
    (docs_dir / 'api.md').write_text('# API Reference\n\nThis page contains the API reference.')
    (docs_dir / 'contributing.md').write_text('# Contributing\n\nGuidelines for contributing to the project.')

    # Add mkdocs dependencies to development requirements
    with open('pyproject.toml', 'a') as f:
        f.write('\n[tool.poetry.group.docs]\n')
        f.write('dependencies = [\n')
        f.write('    "mkdocs>=1.4.0",\n')
        f.write('    "mkdocs-material>=9.0.0",\n')
        f.write('    "mkdocstrings>=0.20.0",\n')
        f.write('    "mkdocstrings-python>=0.9.0"\n')
        f.write(']\n')

    # Add documentation commands to Makefile
    with open('Makefile', 'a') as f:
        f.write('\n.PHONY: docs serve-docs\n\n')
        f.write('docs:\n\tmkdocs build\n\n')
        f.write('serve-docs:\n\tmkdocs serve\n')


def additional_features():
    if "{{ cookiecutter.include_docker }}" != "True":
        remove_docker_file()

    if "{{ cookiecutter.include_mkdocs }}" == "True":
        setup_mkdocs()
    else:
        # Remove mkdocs config if not needed
        if os.path.exists('mkdocs.yml'):
            os.remove('mkdocs.yml')
        if os.path.exists('docs'):
            shutil.rmtree('docs')

def setup_venv() -> None:
    python_version = "{{ cookiecutter.python_version }}"
    try:
        subprocess.run(
            [f"python{python_version}", "-m", "venv", ".venv"],
            check=True
        )
    except:
        print(f"Warning: Python {python_version} not found, using default version")
        subprocess.run(
            ["python", "-m", "venv", ".venv"],
            check=True
        )

def main():
    try:
        additional_features()

        setup_venv()

        print("\n✨ Project setup complete!")
    except Exception as e:
        print(f"⚠️  An error occurred during setup: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
