# genpark-izhikevich-spiking-neuron-bursting-skill

[![Agentic Skill](https://img.shields.io/badge/GenPark-Agentic__Skill-blue.svg)](https://github.com/Alpha-Park/genpark-izhikevich-spiking-neuron-bursting-skill)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://python.org)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-0%20Pip-orange.svg)](#)
[![Dual Org Verified](https://img.shields.io/badge/GitHub-Dual__Org-purple.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Izhikevich phenomenological spiking neuron model reproducing tonic spiking, phasic spiking, and chattering bursting patterns via two coupled 2D ODEs.

## Architecture Overview

```mermaid
flowchart TD
    A[Agentic AI / Neuromorphic Task] -->|Input Spikes / Currents| B[MCP Server / Client]
    B --> C[genpark-izhikevich-spiking-neuron-bursting-skill Engine]
    C --> D[Differential Equation / Dynamic State Update]
    D --> E[Spike Events & Synaptic Adaptation]
    E -->|Structured Event Output| A
```

## Features
- **0 External Pip Dependencies**: Pure Python standard library implementation.
- **MCP Protocol Ready**: Includes Model Context Protocol server script (`mcp_server.py`).
- **Production Standard**: Comprehensive numerical validation, unit test coverage, and benchmark speed.

## Quick Start
```bash
python example_usage.py
```
