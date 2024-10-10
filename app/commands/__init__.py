"""This module contains the Command and CommandHandler classes"""

from abc import ABC, abstractmethod
import logging


class Command(ABC):
    """Abstract base class for commands."""

    @abstractmethod
    def execute(self):
        """Base method for executing a command."""


class CommandHandler:
    """This class is responsible for registering and executing commands."""

    def __init__(self):
        self.commands: dict[str, Command] = {}

    def register_command(self, command_name: str, command: Command):
        """Register a command with the handler."""
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """Execute a command by name."""
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")
