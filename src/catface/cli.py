import importlib
import subprocess
from pathlib import Path

import click
import questionary
from cookiecutter.main import cookiecutter
from rich.console import Console
from rich.panel import Panel

console = Console()


def get_template_path():
    with importlib.resources.path("catface", "template") as template_path:
        return str(template_path)


def validate_project_name(name: str) -> bool:
    return all(c.isalnum() or c in ("-", "_") for c in name)


@click.command()
@click.argument("project_name", required=False)
def main(project_name: str):
    """Create a new Python project with best practices and modern tooling."""
    console.print(Panel.fit("Create Python App", style="bold blue"))

    # Get project details through interactive prompts
    if not project_name:
        project_name = questionary.text(
            "What is your project name?",
            validate=lambda text: len(text) > 0 and validate_project_name(text),
        ).ask()

    features = questionary.checkbox(
        "Select additional features:",
        choices=[
            "Docker",
            "Pre-commit hooks",
            "Documentation (MKDocs)",
        ],
    ).ask()

    python_version = questionary.select(
        "Select Python version:", choices=["3.11", "3.12"]
    ).ask()

    # Create project context
    context = {
        "project_name": project_name,
        "project_slug": project_name.lower().replace(" ", "_"),
        "python_version": python_version,
        "include_docker": "Docker" in features,
        "include_precommit": "Pre-commit hooks" in features,
        "include_mkdocs": "Documentation (MKDocs)" in features,
    }

    template_path = get_template_path()

    with console.status("[bold green]Creating project..."):
        # Create project using cookiecutter
        project_path = Path.cwd() / project_name
        cookiecutter(
            str(template_path),
            no_input=True,
            extra_context=context,
            output_dir=str(Path.cwd()),
        )

        # Install development dependencies
        subprocess.run(
            ["pip", "install", "-e", "."], cwd=project_path, capture_output=True
        )

    console.print(f"\n✨ Successfully created project [bold green]{project_name}[/]!")
    console.print("\nNext steps:")
    console.print("  1. cd", project_name)
    console.print("  2. tox -e <env_name> or tox")
