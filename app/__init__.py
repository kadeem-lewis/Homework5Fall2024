"""Main application module."""

from app.commands import CommandHandler
from app.commands.greet import GreetCommand
from app.commands.menu import MenuCommand
from app.commands.exit import ExitCommand
from app.commands.github import GithubCommand
from app.commands.goodbye import GoodbyeCommand


class App:
    """Main application class."""

    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self):
        """Start the application."""
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("github", GithubCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())

        print("Type 'exit' to exit.")
        while True:  # REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(">>> ").strip())
