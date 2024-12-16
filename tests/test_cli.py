from click.testing import CliRunner


def test_project_creation():
    """Test basic project creation with CLI."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        pass
