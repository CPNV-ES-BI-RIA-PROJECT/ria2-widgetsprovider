"""Factory for creating widget providers."""
import os

from .widget_provider import WidgetProvider
from .models.widget_provider_interface import WidgetProviderInterface
from .models.bucket_widget_provider import BucketWidgetProvider

def get_provider() -> WidgetProviderInterface:
    """Create a widget provider based on the provider type."""
    provider = WidgetProvider(os.getenv("WIDGET_PROVIDER", "bucket"))

    match provider:
        case WidgetProvider.BUCKET:
            return BucketWidgetProvider()
        case _:
            raise ValueError(f"Unknown provider type: {provider}")
