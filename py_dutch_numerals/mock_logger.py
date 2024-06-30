from .logger import Logger

class MockLogger(Logger):
    def __init__(self):
        self.error_logs = []
        self.info_logs = []
        self.warning_logs = []

    def log_error(self, message: str) -> None:
        self.error_logs.append(message)

    def log_info(self, message: str) -> None:
        self.info_logs.append(message)

    def log_warning(self, message: str) -> None:
        self.warning_logs.append(message)
