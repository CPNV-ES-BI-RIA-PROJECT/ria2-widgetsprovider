"""Common assertions for widget provider tests."""
import pytest

from app.services.widget_service.exceptions import WidgetNotFoundError

class ProviderTestAssertions:
    """Common assertions for widget provider tests."""

    expected_widget_ids = ["first-widget.html", "second-widget.html"]
    expected_widget_map = {
        "first-widget.html": "First Widget",
        "second-widget.html": "Second Widget",
    }
    expected_widget_link = "https://bucket.local/first-widget.html"

    def assert_list_widgets(self, provider):
        """Asserts that list returns a dict of widget ids and names."""
        widgets = provider.list()

        assert isinstance(widgets, dict)
        assert widgets == self.expected_widget_map

    def assert_list_widgets_empty(self, provider):
        """Asserts that list returns an empty dict when provider has no widgets."""
        widgets = provider.list()

        assert isinstance(widgets, dict)
        assert widgets == {}

    def assert_get_widget_link(self, provider):
        """Asserts that get returns a non-empty public link string."""
        link = provider.get("first-widget.html")

        assert isinstance(link, str)
        assert link == self.expected_widget_link

    def assert_get_widget_link_not_found(self, provider):
        """Asserts that WidgetNotFoundError is raised when widget is not found."""
        with pytest.raises(WidgetNotFoundError):
            provider.get("missing-widget.html")
