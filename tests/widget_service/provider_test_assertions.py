"""Common assertions for widget provider tests."""
import pytest

from app.services.widget_service.exceptions import WidgetNotFoundError

class ProviderTestAssertions:
    """Common assertions for widget provider tests."""

    expected_widget_link = "https://bucket.local/first-widget.html"

    def assert_list_widgets(self, provider, expected_widgets):
        """Asserts that list returns a dict of widget ids and names."""
        widgets = provider.list()

        assert isinstance(widgets, dict)
        assert widgets == expected_widgets

    def assert_list_widgets_empty(self, provider):
        """Asserts that list returns an empty dict when provider has no widgets."""
        widgets = provider.list()

        assert isinstance(widgets, dict)
        assert widgets == {}

    def assert_get_widget_link(self, provider, expected_link):
        """Asserts that get returns a non-empty public link string."""
        link = provider.get("first-widget.html")

        assert isinstance(link, str)
        assert link == expected_link

    def assert_get_widget_link_not_found(self, provider):
        """Asserts that WidgetNotFoundError is raised when widget is not found."""
        with pytest.raises(WidgetNotFoundError):
            provider.get("missing-widget.html")
