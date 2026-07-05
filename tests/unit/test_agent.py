"""CEO Copilot Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_synthesize_performance():
    """Test Synthesize company-wide performance metrics and trends."""
    tools = AgentTools()
    result = await tools.synthesize_performance(period="test", focus_areas="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_prepare_board_materials():
    """Test Prepare board meeting materials and presentations."""
    tools = AgentTools()
    result = await tools.prepare_board_materials(meeting_date="test", agenda_items="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_track_strategic_initiatives():
    """Test Track progress on strategic initiatives and OKRs."""
    tools = AgentTools()
    result = await tools.track_strategic_initiatives(initiatives="test", period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_monitor_competitive_landscape():
    """Test Monitor competitive moves and market trends."""
    tools = AgentTools()
    result = await tools.monitor_competitive_landscape(competitors="test", signals="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.ceo_copilot_agent_agent import CeoCopilotAgentAgent
    agent = CeoCopilotAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
