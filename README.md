# CEO Copilot Agent

[![CI](https://github.com/kogunlowo123/ceo-copilot-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/ceo-copilot-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Executive | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

CEO copilot agent that synthesizes company performance data, prepares board meeting materials, tracks strategic initiatives, monitors competitive landscape, and provides decision support for executive leadership.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `synthesize_performance` | Synthesize company-wide performance metrics and trends |
| `prepare_board_materials` | Prepare board meeting materials and presentations |
| `track_strategic_initiatives` | Track progress on strategic initiatives and OKRs |
| `monitor_competitive_landscape` | Monitor competitive moves and market trends |
| `generate_decision_brief` | Generate a decision brief with options and trade-offs |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/ceo-copilot/synthesize` | Synthesize data |
| `POST` | `/api/v1/ceo-copilot/analyze` | Analyze |
| `GET` | `/api/v1/ceo-copilot/track` | Track metrics |
| `POST` | `/api/v1/ceo-copilot/recommend` | Get recommendation |
| `POST` | `/api/v1/ceo-copilot/report` | Generate report |

## Features

- Ceo
- Copilot
- Strategic Insights
- Decision Support

## Integrations

- Snowflake
- Tableau
- Salesforce
- Workday
- Jira

## Architecture

```
ceo-copilot-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── ceo_copilot_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Enterprise Data Platform + LLM + BI**

---

Built as part of the Enterprise AI Agent Platform.
