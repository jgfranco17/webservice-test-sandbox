import logging
import os

import uvicorn

from backend.core.constants import DEFAULT_HOST, DEFAULT_PORT
from backend.service import app

logger = logging.getLogger(__name__)
logging.basicConfig(
    format="[%(asctime)s][%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG,
)


def run_server() -> None:
    """Run the backend service."""
    host = DEFAULT_HOST
    port = DEFAULT_PORT
    if port_from_env := os.getenv("SANBOX_SERVER_PORT"):
        port = int(port_from_env)
        logger.info(f"Using port from environment: {port_from_env}")

    logger.debug(f"Starting server on {host}:{port}")
    uvicorn.run(app, host=host, port=port)
