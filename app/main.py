"""Main application file for the FastAPI web service."""
from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI

from app.config.container import Container
from app.controllers import widgets_controller
from app.services.widget_service.models import bucket_widget_provider
from app.services.widget_service.models import metabase_widget_provider

container = Container()
container.wire(modules=[widgets_controller, bucket_widget_provider, metabase_widget_provider])

app = FastAPI()
load_dotenv()

app.include_router(widgets_controller.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
