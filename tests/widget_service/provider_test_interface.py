"""Contract tests for widget provider implementations."""
import pytest

class ProviderTestInterface:
    """Reusable test contract for all widget provider implementations."""

    @pytest.fixture
    def container(self):
        """Fixture to provide dependency injection container."""
        raise NotImplementedError

    @pytest.fixture
    def client(self, container, mocker):
        """Fixture to mock bucket service client."""
        raise NotImplementedError

    @pytest.fixture
    def provider(self, client):
        """Fixture to create a provider adapter with mocked client."""
        raise NotImplementedError

    def test_list_widgets(self, provider, client):
        """Provider must list available widgets."""
        raise NotImplementedError

    def test_list_empty(self, provider, client):
        """Provider must return empty dict when no widgets are available."""
        raise NotImplementedError

    def test_get_link(self, provider, client):
        """Provider must return a valid public link for an existing widget."""
        raise NotImplementedError

    def test_get_link_widget_not_found(self, provider, client):
        """Provider must raise an error when requested widget id does not exist."""
        raise NotImplementedError
