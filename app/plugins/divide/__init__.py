"""Divide command plugin"""

from app.commands import Command
from app.calculator import Calculator


class DivideCommand(Command):
    """Command to divide two numbers"""

    def execute(self, num_one, num_two):
        """Divide two numbers"""
        return Calculator.divide(num_one, num_two)
