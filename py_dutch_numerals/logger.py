from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log_error(self, message: str) -> None:
        """Log an error message."""
        pass

    @abstractmethod
    def log_info(self, message: str) -> None:
        """Log an info message."""
        pass

    @abstractmethod
    def log_warning(self, message: str) -> None:
        """Log a warning message."""
        pass
