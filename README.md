# AI Risk Detector — DevOps AI Assistant

**Agile Project Management — Group 5**

AI Risk Detector is an AI-supported MVP designed to help Agile and DevOps software teams identify risks, improve backlog quality and generate better user stories before implementation or release.

The project was developed for the **Agile Project Management** course. Its main goal is not to build a complex production-ready software platform, but to demonstrate how **Agile, Scrum, DevOps and responsible AI concepts** can be applied in a realistic product context.

---

## 1. Project Summary

Software teams working in Agile and DevOps environments often need to deliver quickly while managing uncertainty, technical complexity and changing requirements.

However, teams may face problems such as:

- unclear or poorly structured backlog items;
- ambiguous requirements;
- missing acceptance criteria;
- weak visibility of technical and delivery risks;
- insufficient testing preparation;
- lack of release readiness checks;
- rework caused by late identification of problems.

AI Risk Detector addresses this problem by providing a lightweight assistant that analyses a software task, requirement or idea and returns both:

1. a structured **risk analysis**;
2. a generated **user story** suitable for Jira or Product Backlog refinement.

---

## 2. Proposed Solution

The user enters a software task or requirement, for example:

`Deploy the new authentication module to production without a rollback plan.`

The app then generates:

- Risk Level;
- Risk Score;
- Potential Risks;
- Estimated Impact;
- Mitigation Recommendations;
- Suggested Tests;
- Release Readiness Notes;
- Backlog Improvement Suggestions;
- Generated User Story;
- Acceptance Criteria in Given / When / Then format;
- Suggested Priority;
- Suggested Story Points;
- Suggested Epic;
- Clarification Questions;
- Definition of Ready checklist;
- Human Validation Note.

The assistant is intended to support discussion and decision-making. It does not replace the responsibility of the Product Owner, Scrum Master, Developers or other stakeholders.

---

## 3. MVP Scope

The MVP focuses on demonstrating the core value of the product:

> helping Agile and DevOps teams identify risks earlier and improve backlog quality before work starts.

The MVP is intentionally simple and lightweight.

### In Scope

- Task or requirement input.
- Risk analysis.
- User story generation.
- Acceptance criteria generation.
- Suggested tests.
- Release readiness notes.
- Backlog improvement suggestions.
- Responsible AI disclaimer.
- Local execution with Streamlit.
- Automated tests with pytest.
- CI pipeline with GitHub Actions.

### Out of Scope

- Full production AI platform.
- Real Jira API integration.
- User authentication.
- Database storage.
- Real-time monitoring.
- Enterprise deployment.
- Use of a paid external AI API.

---

## 4. AI Prototype Approach

This MVP does not use a real external AI API.

Instead, it uses deterministic rule-based logic to simulate how an AI-supported assistant could help software teams analyse risk and improve backlog items.

This decision was intentional because the main objective of the project is to demonstrate **Agile Project Management, Scrum and DevOps practices**, not to build a production-ready AI system.

In a real production environment, the rule-based logic could later be replaced or extended with a Large Language Model, subject to validation, governance and responsible AI controls.

---

## 5. Scrum and Jira

Jira was used as the Scrum management tool for the project.

Jira contains:

- Epics;
- Product Backlog items;
- User Stories;
- Acceptance Criteria;
- Priority information;
- Story Points;
- Sprint allocation;
- workflow visibility.

The workflow used in Jira is:

`To Do -> In Progress -> In Review -> Done`

### Jira Board

The Jira project can be accessed here:

`https://airiskdetectorgroup5.atlassian.net/jira/software/projects/SCRUM/summary`

---

## 6. DevOps Evidence

The project includes basic DevOps evidence through:

- GitHub repository and version control;
- automated tests using pytest;
- GitHub Actions CI pipeline;
- clear project structure;
- repeatable local execution;
- MVP delivery;
- documentation of limitations and future improvements.

The DevOps approach is understood not only as automation, but also as a way to improve quality, feedback, delivery reliability and collaboration.

---

## 7. How to Run the App

Install dependencies:

`pip install -r requirements.txt`

Run the Streamlit app:

`streamlit run src/app.py`

If needed, Streamlit can also be installed directly:

`pip install streamlit`

---

## 8. How to Run Tests

Run the test suite:

`pytest`

If Python cannot find the `src` module, run:

`PYTHONPATH=. pytest`

On Windows PowerShell:

`$env:PYTHONPATH="."`

`pytest`

The tests validate the main MVP logic, including:

- high-risk deployment analysis;
- low-risk documentation changes;
- medium-risk API or integration changes;
- user story generation;
- acceptance criteria generation;
- role inference;
- epic inference;
- valid output structure.

---

## 9. Repository Structure

```text
AI-Risk-Detector/
|
├── .github/
|   └── workflows/
|       └── ci.yml
|
├── docs/
|   ├── 01_project_overview.md
|   ├── 02_product_backlog_scrum.md
|   ├── 03_devops_and_mvp.md
|   └── 04_critical_reflection.md
|
├── src/
|   ├── __init__.py
|   └── app.py
|
├── test/
|   └── test_risk_analyzer.py
|
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
