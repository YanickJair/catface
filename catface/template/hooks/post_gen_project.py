import os
import subprocess
import sys
from pathlib import Path
import shutil


project_name = "{{ cookiecutter.project_name }}"
project_description = "{{ cookiecutter.project_description }}"


def remove_docker_file():
    os.remove('Dockerfile')

def setup_mkdocs():
    """Set up MkDocs documentation."""
    docs_dir = Path('docs')
    docs_dir.mkdir(exist_ok=True)

    # Create initial documentation files
    (docs_dir / 'index.md').write_text(f'# {project_name}\n\n{project_description}')
    (docs_dir / 'api.md').write_text('# API Reference\n\nThis page contains the API reference.')
    (docs_dir / 'contributing.md').write_text('# Contributing\n\nGuidelines for contributing to the project.')

    # Add mkdocs dependencies to development requirements
    with open('requirements.txt', 'a') as f:
        f.write('mkdocs>=1.4.0\n')
        f.write('mkdocs-material>=9.0.0\n')
        f.write('mkdocstrings>=0.20.0\n')
        f.write('mkdocstrings-python>=0.9.0\n')

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

        with open('requirements.txt', 'a') as f:
            f.write('ruff>=0.8.2\n')
            f.write('fastapi>=0.115.6\n')
            f.write('tox>=4.23.2\n')
        print("\n✨ Project setup complete!")
    except Exception as e:
        print(f"⚠️  An error occurred during setup: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
