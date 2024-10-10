"""Main application module."""

from fractions import Fraction
import pkgutil
import importlib
from app.commands import CommandHandler, Command


class App:
    """Main application class."""

    def __init__(self):
        self.command_handler = CommandHandler()

    def load_plugins(self):
        """Dynamically load all plugins in the plugins directory"""
        plugins_package = "app.plugins"
        for index, (_, plugin_name, is_pkg) in enumerate(
            pkgutil.iter_modules([plugins_package.replace(".", "/")]), start=1
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
                            if plugin_name == "menu":
                                self.command_handler.register_command(
                                    plugin_name, item(self.command_handler)
                                )
                                self.command_handler.register_command(
                                    str(index), item(self.command_handler)
                                )
                            else:
                                self.command_handler.register_command(
                                    plugin_name, item()
                                )
                                self.command_handler.register_command(
                                    str(index), item()
                                )
                    except TypeError:
                        continue  # If item is not a

    def start(self):
        """Start the application."""
        self.load_plugins()

        print("Type 'exit' to exit.")
        while True:  # REPL Read, Evaluate, Print, Loop
            command = (
                input(
                    "Enter a command (add, subtract, multiply, divide) or 'exit' to quit: "
                )
                .strip()
                .lower()
            )
            if command in ["exit", "menu"]:
                self.command_handler.execute_command(command)
                continue
            try:
                number_one = Fraction(input("Enter first number: "))
                number_two = Fraction(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            self.command_handler.execute_command(command, number_one, number_two)
