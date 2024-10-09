from app.commands import Command, CommandHandler


class MenuCommand(Command):
    """Command to display the list of available commands."""

    def __init__(self, command_handler: CommandHandler):
        self.command_handler = command_handler

    def execute(self):
        commands_list = list(self.command_handler.commands.keys())
        if commands_list:
            print("Available commands:", ", ".join(commands_list))
        else:
            print("No commands available.")
