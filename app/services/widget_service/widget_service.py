"""Widget Service module."""
from .widget_provider_factory import get_provider

class WidgetService:
    """Service for managing widgets."""

    def __init__(self):
        """Initialize the widget service with the appropriate provider."""
        self._provider = get_provider()

    def list_widgets(self) -> dict[str, str]:
        """List all available widgets from the provider."""
        return self._provider.list()

    def get_widget_link(self, widget_id: str) -> str:
        """Get the public link of a widget by its id."""
        return self._provider.get(widget_id)
