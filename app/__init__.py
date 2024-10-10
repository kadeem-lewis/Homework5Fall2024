"""Main application module."""

import pkgutil
import importlib
from app.commands import CommandHandler, Command
from app.commands.greet import GreetCommand
from app.commands.menu import MenuCommand
from app.commands.exit import ExitCommand
from app.commands.github import GithubCommand
from app.commands.goodbye import GoodbyeCommand


class App:
    """Main application class."""

    def __init__(self):
        self.command_handler = CommandHandler()

    def load_plugins(self):
        """Dynamically load all plugins in the plugins directory"""
        plugins_package = "app.plugins"
        for _, plugin_name, is_pkg in pkgutil.iter_modules(
            [plugins_package.replace(".", "/")]
        ):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(
                    f"{plugins_package}.{plugin_name}"
                )
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(
                            item, (Command)
                        ):  # Assuming a BaseCommand class exists
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # If item is not a

    def start(self):
        """Start the application."""
        # self.load_plugins()

        print("Type 'exit' to exit.")
        while True:  # REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(">>> ").strip())
