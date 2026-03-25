"""Provider for bucket widgets."""
import os
from dependency_injector.wiring import inject, Provide

from .widget_provider_interface import WidgetProviderInterface
from ..exceptions import WidgetNotFoundError

class MetabaseWidgetProvider(WidgetProviderInterface):
    """Provider for bucket widgets."""

    @inject
    def __init__(self, client = Provide['http_client']) -> None:
        """Initialize the bucket widget provider with an HTTP client."""
        self._client = client
        self._url = os.getenv("PROVIDER_METABASE_SERVICE_URL")

    def list(self) -> dict[str, str]:
        """List all available metabase widgets."""
        response = self._client.get(
            f"{self._url}/api/card",
            timeout=20,
            headers={"X-API-Key": os.getenv("PROVIDER_METABASE_API_KEY")},
        )

        return {obj.get("id"): obj.get("name") for obj in response.json()}

    def get(self, widget_id: str) -> str:
        """Get the public link of a metabase widget by its id."""
        response = self._client.post(
            f"{self._url}/api/card/{widget_id}/public_link",
            timeout=20,
            headers={"X-API-Key": os.getenv("PROVIDER_METABASE_API_KEY")},
        )

        if response.status_code == 404:
            raise WidgetNotFoundError()

        public_id = response.json().get("uuid")
        link = f"{self._url}/public/question/{public_id}"

        return link
