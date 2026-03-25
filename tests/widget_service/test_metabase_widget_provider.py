"""Tests for MetabaseWidgetProvider implementation of WidgetProviderInterface."""
import pytest

from app.config.container import Container
from app.services.widget_service.models.metabase_widget_provider import MetabaseWidgetProvider
from .provider_test_interface import ProviderTestInterface
from .provider_test_assertions import ProviderTestAssertions

class TestMetabaseWidgetProvider(ProviderTestInterface, ProviderTestAssertions):
    """Tests for MetabaseWidgetProvider implementation of WidgetProviderInterface."""

    @pytest.fixture
    def container(self):
        """Fixture to provide dependency injection container."""
        container = Container()
        container.wire(modules=[MetabaseWidgetProvider])
        return container

    @pytest.fixture
    def client(self, container, mocker):
        """Fixture to mock metabase service client."""
        mocked_client = mocker.Mock()
        with container.http_client.override(mocked_client):
            yield mocked_client

    @pytest.fixture
    def provider(self, client):
        """Fixture to create a provider adapter with mocked client."""
        pytest.MonkeyPatch().setenv("PROVIDER_METABASE_SERVICE_URL", "https://metabase.local")
        return MetabaseWidgetProvider()

    def test_list_widgets(self, provider, client):
        """Provider must list available widgets."""
        response = client.get.return_value
        response.status_code = 200
        response.json.return_value = [
            {"id": 38, "name": "First Widget", "other_field": "value1"},
            {"id": 39, "name": "Second Widget", "other_field": "value2"},
        ]

        expected_values = {
            38: "First Widget",
            39: "Second Widget",
        }

        self.assert_list_widgets(provider, expected_values)

    def test_list_empty(self, provider, client):
        """Provider must return empty dict when no widgets are available."""
        response = client.get.return_value
        response.status_code = 200
        response.json.return_value = []

        self.assert_list_widgets_empty(provider)

    def test_get_link(self, provider, client):
        """Provider must return a valid public link for an existing widget."""
        response = client.post.return_value
        response.status_code = 200
        response.json.return_value = {"uuid": "aaaa-bbbb-cccc-dddddddddddd"}

        expected_widget_link = "https://metabase.local/public/question/aaaa-bbbb-cccc-dddddddddddd"

        self.assert_get_widget_link(provider, expected_widget_link)

    def test_get_link_widget_not_found(self, provider, client):
        """Provider must raise an error when requested widget id does not exist."""
        response = client.post.return_value
        response.status_code = 404

        self.assert_get_widget_link_not_found(provider)
