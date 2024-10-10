"""Tests for the command functions."""

import pytest
from app import App
from app.plugins.goodbye import GoodbyeCommand
from app.plugins.greet import GreetCommand
from app.plugins.github import GithubCommand


def test_greet_command(capfd):
    """Test that the GreetCommand prints 'Hello, World!'."""
    command = GreetCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "Hello, World!\n", "The GreetCommand should print 'Hello, World!'"


def test_goodbye_command(capfd):
    """Test that the GoodbyeCommand prints 'Goodbye'."""
    command = GoodbyeCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "Goodbye\n", "The GreetCommand should print 'Hello, World!'"


def test_github_command(capfd):
    """Test that the GithubCommand prints"""
    command = GithubCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "https://github.com/kadeem-lewis/Homework5Fall2024\n"


def test_app_greet_command(monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(["greet", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert str(e.value) == "Exiting...", "The app did not exit as expected"


def test_app_menu_command(monkeypatch, capfd):
    """Test that the REPL correctly handles the 'menu' command and prints available commands."""
    # Simulate user entering 'menu' followed by 'exit'
    inputs = iter(["menu", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) as e:
        app.start()

    # Capture the output of the 'menu' command
    out, _ = capfd.readouterr()

    # Verify that the expected menu content appears in the output
    expected_commands = ["greet", "goodbye", "github", "menu", "exit"]

    assert str(e.value) == "Exiting...", "The app did not exit as expected"

    # Check that the output contains the available commands
    for command in expected_commands:
        assert command in out, f"The command '{command}' should be listed in the menu."
