"""
This module defines the WidgetProviderInterface,
which is an abstract base class that specifies the methods that any widget provider must implement.
"""
from abc import ABC, abstractmethod

class WidgetProviderInterface(ABC):
    """Interface for widgets providers."""

    @abstractmethod
    def list(self) -> dict[str, str]:
        """Returns a list of all widgets with their id and name."""

    @abstractmethod
    def get(self, widget_id: str) -> str:
        """Returns the public link of the widget with the given id."""
