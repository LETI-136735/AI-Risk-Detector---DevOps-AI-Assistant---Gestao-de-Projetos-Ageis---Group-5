# AI Risk Detector - DevOps AI Assistant

Agile Project Management - Group 5

AI Risk Detector is an AI-supported assistant for Agile and DevOps software teams. It helps analyse software tasks, requirements, or user stories before implementation so the team can identify risks, improve backlog quality, and discuss testing or release readiness earlier.

The project was created for a university Agile Project Management assignment. The main goal is to demonstrate Agile, Scrum, DevOps, MVP thinking, and responsible AI use in a coherent project context.

## Project Summary

The assistant receives a software work item written in natural language and returns a structured risk analysis.

The expected output includes:

- Risk level
- Potential risks
- Expected impact
- Mitigation recommendations
- Suggested tests
- Possible acceptance criteria
- Backlog improvement suggestions

The AI output supports team discussion. It does not replace human judgement from the Product Owner, Scrum Master, Developers, or stakeholders.

## Documentation

The documentation has been simplified into four main files:

- [Project Overview](docs/01_project_overview.md)
- [Product Backlog and Scrum](docs/02_product_backlog_scrum.md)
- [DevOps and MVP](docs/03_devops_and_mvp.md)
- [Critical Reflection](docs/04_critical_reflection.md)

Older documentation and management files were moved to the archive folders:

- `archive/old_docs/`
- `archive/old_management/`

## Jira Board

Jira board link:

[Insert Jira board link here]

The Jira board contains the operational Scrum evidence for the project, including:

- Epics
- Product Backlog
- User Stories
- Acceptance Criteria
- Priority Score 1-4
- Story Points
- Sprint allocation
- Workflow: To Do -> In Progress -> In Review -> Done

The Jira board will be presented online, so separate management documentation is not required in the main repository structure.

## MVP Scope

The MVP focuses on the simplest useful version of the product:

- Enter a software task, requirement, or user story
- Generate a risk level
- Identify potential risks
- Explain the possible impact
- Suggest mitigation actions
- Suggest tests
- Propose acceptance criteria
- Improve backlog clarity

The MVP does not include full Jira API integration, production monitoring, or a complete DevOps platform. These are future improvements.

## Repository Structure

```text
AI-Risk-Detector/
|
+-- README.md
+-- docs/
|   +-- 01_project_overview.md
|   +-- 02_product_backlog_scrum.md
|   +-- 03_devops_and_mvp.md
|   +-- 04_critical_reflection.md
+-- archive/
|   +-- old_docs/
|   +-- old_management/
+-- src/
+-- test/
+-- .github/
+-- requirements.txt
```

## Responsible AI Note

AI Risk Detector is a support tool. Its recommendations must be reviewed by humans before being used for real planning, development, testing, or release decisions.
