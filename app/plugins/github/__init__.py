"""Module to show link to GitHub repository."""

from app.commands import Command


class GithubCommand(Command):
    """Command to show link to GitHub repository."""

    def execute(self):
        print("https://github.com/kadeem-lewis/Homework5Fall2024")
