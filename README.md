EKDPA – Knowledge Guardian Agent

EKDPA (Enterprise Knowledge Defense & Preservation Agent) is an agentic AI solution built using IBM watsonx Orchestrate to proactively detect and mitigate organizational knowledge loss.

🚨 Problem
Critical enterprise knowledge is often concentrated in a small number of employees and remains undocumented. When these employees leave or become unavailable, organizations face operational disruption, compliance risk, and financial loss.

💡 Solution
EKDPA continuously evaluates roles and employees for knowledge-at-risk using:
- Documentation coverage
- Role criticality
- Knowledge ownership redundancy

When high risk is detected, the Knowledge Guardian Agent orchestrates:
- Structured knowledge capture
- Peer validation (human-in-the-loop)
- Backup owner assignment
- Secure knowledge closure

🧠 Agentic AI & Orchestration
IBM watsonx Orchestrate acts as the control plane for:
- Decision-making
- Workflow branching
- Long-running human-in-the-loop processes
- Multi-step status transitions (HIGH → IN_PROGRESS → SECURED)

📂 Repository Contents
- `/code` – Reference Python logic representing agent decisions
- `/docs` – Knowledge risk policy documentation
- `/sample_inputs` – Demo-ready test cases

🎥 Demo
See the 3-minute video demonstration for the full workflow execution using watsonx Orchestrate.

## ⚠️ Note
This repository is a conceptual reference. The live orchestration and agent execution occur within IBM watsonx Orchestrate.
