"""Tests for BucketWidgetProvider implementation of WidgetProviderInterface."""
import pytest

from app.config.container import Container
from app.services.widget_service.models.bucket_widget_provider import BucketWidgetProvider
from .provider_test_interface import ProviderTestInterface
from .provider_test_assertions import ProviderTestAssertions

class TestBucketWidgetProvider(ProviderTestInterface, ProviderTestAssertions):
    """Tests for BucketWidgetProvider implementation of WidgetProviderInterface."""

    @pytest.fixture
    def container(self):
        """Fixture to provide dependency injection container."""
        container = Container()
        container.wire(modules=[BucketWidgetProvider])
        return container

    @pytest.fixture
    def client(self, container, mocker):
        """Fixture to mock bucket service client."""
        mocked_client = mocker.Mock()
        with container.http_client.override(mocked_client):
            yield mocked_client

    @pytest.fixture
    def provider(self, client):
        """Fixture to create a provider adapter with mocked client."""
        return BucketWidgetProvider()

    def test_list_widgets(self, provider, client):
        """Provider must list available widgets."""
        response = client.get.return_value
        response.status_code = 200
        response.json.return_value = self.expected_widget_ids

        self.assert_list_widgets(provider)

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
        response.json.return_value = {"shareable_link": self.expected_widget_link}

        self.assert_get_widget_link(provider)

    def test_get_link_widget_not_found(self, provider, client):
        """Provider must raise an error when requested widget id does not exist."""
        response = client.post.return_value
        response.status_code = 404

        self.assert_get_widget_link_not_found(provider)
