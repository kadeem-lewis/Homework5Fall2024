"""Main application module."""

from app.commands import CommandHandler
from app.commands.greet import GreetCommand
from app.commands.menu import MenuCommand
from app.commands.exit import ExitCommand


class App:
    """Main application class."""

    def __init__(self):  # Constructor
        self.command_handler = CommandHandler()

    def start(self):
        """Start the application."""
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))
        self.command_handler.register_command("exit", ExitCommand())

        print("Type 'exit' to exit.")
        while True:  # REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(">>> ").strip())
