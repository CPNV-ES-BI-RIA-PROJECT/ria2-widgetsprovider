"""Widget provider enumeration"""
from enum import Enum

class WidgetProvider(Enum):
    """Enumeration of supported widget providers."""
    BUCKET = "bucket"
    METABASE = "metabase"
