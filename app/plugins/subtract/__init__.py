"""Subtract command plugin"""

from app.commands import Command
from app.calculator import Calculator


class SubtractCommand(Command):
    """Command to subtract two numbers"""

    def execute(self, num_one, num_two):
        """Subtract two numbers"""
        return Calculator.subtract(num_one, num_two)
