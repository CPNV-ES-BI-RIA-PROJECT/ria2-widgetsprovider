"""Provider for bucket widgets."""
import os
from dependency_injector.wiring import inject, Provide

from .widget_provider_interface import WidgetProviderInterface
from ..exceptions import WidgetNotFoundError

class BucketWidgetProvider(WidgetProviderInterface):
    """Provider for bucket widgets."""

    @inject
    def __init__(self, client = Provide['http_client']) -> None:
        """Initialize the bucket widget provider with an HTTP client."""
        self._client = client
        self._url = os.getenv("PROVIDER_BUCKET_SERVICE_URL")
        self._bucket_name = os.getenv("PROVIDER_BUCKET_NAME")

    def list(self) -> dict[str, str]:
        """List all available bucket widgets."""
        response = self._client.get(
            f"{self._url}/api/v1/objects?remote_src={self._bucket_name}%2F",
            timeout=20
        )

        return {obj: self._id_to_name(obj) for obj in response.json()}

    def get(self, widget_id: str) -> str:
        """Get the public link of a bucket widget by its id."""
        response = self._client.post(
            f"{self._url}/api/v1/objects/{self._bucket_name}%2F{widget_id}",
            timeout=20
        )

        if response.status_code == 404:
            raise WidgetNotFoundError()

        return response.json().get("shareable_link")

    def _id_to_name(self, widget_id: str) -> str:
        """Convert a widget id to its name."""
        name = widget_id.replace("-", " ").replace(".html", "").title()

        return name
