class SafetyEngine:

    def __init__(self):

        self.dangerous_commands = [

            "rm -rf",

            "mkfs",

            "dd ",

            ":(){",

            "shutdown",

            "reboot",

            "halt",

            "poweroff",

            "init 0",

            "init 6",

            "chmod 777 /",

            "chown -R",

            "userdel -r",

            "kill -9 1"

        ]

    def validate(self, commands):

        """
        Validate a list of Linux commands.

        Returns:
            (True, None) if all commands are safe.
            (False, command) if a dangerous command is found.
        """

        for command in commands:

            command_lower = command.lower()

            for dangerous in self.dangerous_commands:

                if dangerous in command_lower:

                    return False, command

        return True, None