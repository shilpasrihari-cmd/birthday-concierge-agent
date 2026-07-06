# birthday-concierge-agent

An AI-powered multi-agent system that plans a birthday party end-to-end:
- Finds suitable dates
- Recommends venues
- Books the selected venue (with human approval)
- Sends invitations and tracks RSVPs
- Collects dietary restrictions (mocked)
- Coordinates food ordering

## Key Concepts Demonstrated

- **Agent / Multi-agent system (ADK)**  
  - Orchestrator + Intake, Date, Venue, Booking, Invitation, RSVP, Dietary, Food agents.

- **Agent skills (Agents CLI)**  
  - Each agent exposes named skills (e.g., `create_event_spec`, `suggest_dates`, `recommend_venues`, `compose_invitation_email`, `summarize_dietary`, `propose_and_order_food`).

- **MCP Server (tools layer)**  
  - `tools/calendar_tool.py`, `tools/venue_tool.py`, `tools/email_tool.py`, `tools/food_tool.py`.

- **Security features**  
  - Human-in-the-loop confirmations for booking and food ordering.  
  - PII-safe logging (no full email bodies or dietary details).

- **Deployability**  
  - CLI demo via `main.py` that runs the full workflow.

- **Antigravity**  
  - Parallel venue scoring in `VenueAgent` using `ThreadPoolExecutor`.

## Project Structure

```text
birthday-concierge-agent/
├── main.py
├── README.md
├── requirements.txt
├── models.py
├── agents/
│   ├── orchestrator.py
│   ├── intake_agent.py
│   ├── date_agent.py
│   ├── venue_agent.py
│   ├── booking_agent.py
│   ├── invitation_agent.py
│   ├── rsvp_agent.py
│   ├── dietary_agent.py
│   └── food_agent.py
└── tools/
    ├── calendar_tool.py
    ├── venue_tool.py
    ├── email_tool.py
    └── food_tool.py
