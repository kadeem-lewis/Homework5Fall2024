"""Command to say goodbye to the user"""

from app.commands import Command


class GoodbyeCommand(Command):
    """Command to say goodbye to the user"""

    def execute(self):
        print("Goodbye")
