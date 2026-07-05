"""Test configuration for CEO Copilot Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "ceo-copilot-agent", "category": "Executive"}
