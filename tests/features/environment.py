import logging
import os
import shutil

from behave.model import Scenario

from tests.shared.client import ServiceClient
from tests.shared.stubs import TestContext

logger = logging.getLogger(__name__)


def before_all(context: TestContext):
    """Initialize shared context data."""
    context.client = ServiceClient(port=8080)
    logger.info("Starting test suite, service client initialized...")


def before_scenario(context: TestContext, scenario: Scenario):
    """Initialize shared context data."""
    context.last_response = None
    context.last_exception = None
    logger.debug(f"Starting scenario: {scenario.name}")


def after_scenario(context: TestContext, scenario: Scenario):
    """Clean up shared context data after a scenario."""
    context.last_exception = None
    logger.info(f"Scenario '{scenario.name}' ran in {scenario.duration:.2f}s")
