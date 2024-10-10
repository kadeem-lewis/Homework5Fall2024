"""Multiply command plugin"""

from app.commands import Command
from app.calculator import Calculator


class MultiplyCommand(Command):
    """Command to multiply two numbers"""

    def execute(self, num_one, num_two):
        """Multiply two numbers"""
        print(Calculator.multiply(num_one, num_two))
