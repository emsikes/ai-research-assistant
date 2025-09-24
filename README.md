# 🤖 AI Research Assistant

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)\
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)\
[![Build
Status](https://img.shields.io/github/actions/workflow/status/emsikes/ai-research-assistant/ci.yml?branch=main)](https://github.com/emsikes/ai-research-assistant/actions)\


> A modular assistant for accelerating AI‑driven research workflows ---
> orchestration of agents for search, planning, writing, and emailing.

------------------------------------------------------------------------

## 🚀 Features

-   **Multi‑agent architecture**: split responsibilities across search,
    planner, writer, email, and management agents\
-   **Deep research support**: interfaces to web / academic search
    engines, summarization, citation handling\
-   **Email / outreach agent**: generate, send, and manage email
    communication within research workflows\
-   **Planner & manager**: orchestrate multi-step tasks, track progress,
    retry logic\
-   **Extensible & modular**: easily add new agents, customize tools,
    swap out components

------------------------------------------------------------------------

## 📦 Getting Started

### Prerequisites

-   Python 3.8 or higher\
-   (Optional) virtual environment tool (e.g. `venv` or `conda`)\
-   API credentials / keys for any external services (e.g. search APIs,
    email provider)

### Installation

``` bash
git clone https://github.com/emsikes/ai-research-assistant.git
cd ai-research-assistant
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Configuration

Copy or rename `.env.example` to `.env` and fill in:

    OPENAI_API_KEY=…
    SEARCH_API_KEY=…
    EMAIL_API_KEY=…
    # Other credentials you require…

### Usage

To launch the assistant with Gradio UI:

``` bash
python deep_research.py
```

This will start a **web interface** where you can enter your research
question directly in the input field and interactively view results.

Example:

1.  Run `python deep_research.py`
2.  Open the link shown in your terminal (e.g. `http://127.0.0.1:7860`)
3.  Enter: *"What are the latest applications of quantum machine
    learning?"*
4.  Results and summaries will be displayed in the browser.

------------------------------------------------------------------------

You can also orchestrate via the planner or run specific agents from the
CLI if preferred:

``` bash
python planner_agent.py --task "Write a literature survey on RL in robotics"
python search_agent.py --query "latest RL in robotics 2025"
python writer_agent.py --outline-file outline.json
```

------------------------------------------------------------------------

## 🧱 Architecture Overview

    User Input ---> Planner Agent ---> Search Agent / Deep Research ---> Writer Agent
                                   \                       /
                                    → Email Agent (optional)
                                   /                       \
                    Manager & Orchestrator module (task coordination, retries, logs)

-   **Planner Agent**: decomposes high-level tasks into subtasks,
    schedules them\
-   **Search & Deep Research Agents**: fetch, filter, summarize
    literature\
-   **Writer Agent**: drafts outputs (reports, summaries, survey
    chapters)\
-   **Email Agent**: compose and send emails (e.g. contacting authors)\
-   **Research Manager**: oversee task flows, logging, error handling,
    state persistence

------------------------------------------------------------------------

## 🛠️ Customization & Extension

-   To add a new search backend, implement the interface in
    `search_agent.py`\
-   For custom writer behavior (e.g. style, tone), override methods in
    `writer_agent.py`\
-   Add new planning strategies or heuristics in `planner_agent.py`\
-   Swap email / notification infrastructure (e.g., send via SMTP,
    SendGrid, etc.)

------------------------------------------------------------------------

## ✅ Best Practices & Guidelines

-   **Modular code**: keep agents decoupled\
-   **Idempotency**: design agents so repeated runs don't break
    consistency\
-   **Logging & tracing**: use structured logs to trace flow across
    agents\
-   **Resource limits & throttling**: manage API quotas, rate limits\
-   **Testing**: unit test core components (search, writer, planner)

------------------------------------------------------------------------

## 🧪 Example Workflow

1.  Call `planner_agent` with a high‑level goal\
2.  Planner splits the goal into sub‑tasks\
3.  `search_agent` / `deep_research` fetch relevant literature\
4.  Data passed to `writer_agent` to draft sections, summaries\
5.  Optionally, `email_agent` sends out inquiries\
6.  Manager monitors, retries, logs progress

------------------------------------------------------------------------

## 📚 References & Credits

-   Built with core dependency on \[OpenAI Python SDK\]\
-   Inspired by agent‑based frameworks in the AI tooling ecosystem\
-   Thanks to contributors and feedback from early users

------------------------------------------------------------------------

## 📄 License

This project is licensed under the **MIT License** --- see `LICENSE`
file for details.

------------------------------------------------------------------------

## 🙋‍♂️ Contribution

Contributions are welcome! To get started:

1.  Fork the repo\
2.  Create a feature branch: `git checkout -b feat/your-feature`\
3.  Commit your changes: `git commit -m "Add X"`\
4.  Push: `git push origin feat/your-feature`\
5.  Open a Pull Request

Please include tests, documentation, and update this README if you add
or change behavior.

------------------------------------------------------------------------

## 🧷 Contact

If you have questions, suggestions or feedback, please open an issue or
reach out to me via GitHub.

------------------------------------------------------------------------
