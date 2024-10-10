"""Command to greet the user"""

from app.commands import Command


class GreetCommand(Command):
    """Command to greet the user"""

    def execute(self):
        print("Hello, World!")
