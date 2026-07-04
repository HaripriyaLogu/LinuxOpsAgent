from datetime import datetime


class AgentLogger:

    def __init__(self, logfile="agent.log"):
        self.logfile = logfile

    def log(self, event, message):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.logfile, "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] [{event}] {message}\n")