"""Add command plugin"""

from app.commands import Command
from app.calculator import Calculator


class AddCommand(Command):
    """Command to add two numbers"""

    def execute(self, num_one, num_two):
        """Add two numbers"""
        print(Calculator.add(num_one, num_two))
