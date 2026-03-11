"""Widgets Controller"""

from typing import Annotated
from fastapi import APIRouter, Path, HTTPException
from dependency_injector.wiring import inject, Provide

from app.services.widget_service.widget_service import WidgetService

router = APIRouter()

@inject
def execute(command: str, *args, service: WidgetService = Provide['widget_service'], **kwargs):
    """Executes a bucket service command with error handling."""
    method = getattr(service, command)

    try:
        return method(*args, **kwargs)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

@router.get("/widgets")
def list_widgets():
    """List all available widgets."""
    return execute("list_widgets")

@router.get("/widgets/{widget_id}")
def get_widget_link(
    widget_id: Annotated[
        str,
        Path(description="The ID of the widget to retrieve")
    ]
):
    """Get the public link of a widget by its id."""
    return execute("get_widget_link", widget_id)
