"""Exceptions for Widget Service."""

class WidgetServiceError(Exception):
    """Base exception class for Widget Service errors."""
    pass

class WidgetNotFoundError(WidgetServiceError):
    """Exception raised when a requested widget is not found."""
    def __init__(self):
        super().__init__("Requested widget not found.")
