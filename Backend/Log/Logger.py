import datetime
import os

class Logger:
    def __init__(self, log_file="./Log/Log.txt"):
        self.log_file = log_file
        self.ensure_file_exists()

    def ensure_file_exists(self):
        if not os.path.isfile(self.log_file):
            with open(self.log_file, "w") as file:
                file.write("Log file created\n")

    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"

        with open(self.log_file, "a") as file:
            file.write(log_entry)