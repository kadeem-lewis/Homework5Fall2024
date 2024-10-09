"""Main application module."""


class App:
    """Main application class."""

    @staticmethod
    def start() -> None:
        """Command to start the application."""
        print("Hello World. Type 'exit' to exit.")

        while True:
            user_input = input(">>> ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break
            print("Unknown command. Type 'exit' to exit.")
