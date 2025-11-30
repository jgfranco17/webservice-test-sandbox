import os
from typing import Final

import pytest

ENV_INTEGRATION_TEST: Final[str] = "RUN_INTEGRATION"


def integration_test(testcase_id: str) -> pytest.MarkDecorator:
    """Mark a test as an integration test."""
    is_integration = os.getenv(ENV_INTEGRATION_TEST) is None
    reason = f"[{testcase_id}] Skipping as this test requires a live instance of server"
    return pytest.mark.skipif(condition=is_integration, reason=reason)
