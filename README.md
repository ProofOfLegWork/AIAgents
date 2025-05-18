# Forum Agent Simulation

This project simulates a forum discussion about cryptocurrency mining using AI agents. The agents have different expertise levels and personalities, and they engage in discussions about proof of work, mining applications, and the future of cryptocurrency mining.

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the simulation:
```bash
python main.py
```

## Features

- Multiple AI agents with different expertise levels (beginner, intermediate, expert)
- Simulated forum discussions on various mining-related topics
- Realistic conversation flow with context-aware responses
- Thread management and discussion summaries

## Project Structure

- `forum_agents/`
  - `base_agent.py`: Base class for all forum agents
  - `mining_agent.py`: Specialized agent for mining discussions
  - `forum_manager.py`: Manages agent interactions and discussions
- `main.py`: Main script to run the simulation
- `requirements.txt`: Project dependencies

## Customization

You can customize the simulation by:
1. Adding more agent types in the `forum_agents` directory
2. Modifying the response templates in `mining_agent.py`
3. Adjusting the discussion duration and topics in `main.py`
