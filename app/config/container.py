"""Dependency Injection Container Configuration."""
from dependency_injector import containers, providers
import requests

from app.services.widget_service.widget_service import WidgetService

class Container(containers.DeclarativeContainer):
    """Dependency Injection Container."""

    http_client = providers.Factory(
        requests.Session,
    )

    widget_service = providers.Singleton(
        WidgetService
    )
