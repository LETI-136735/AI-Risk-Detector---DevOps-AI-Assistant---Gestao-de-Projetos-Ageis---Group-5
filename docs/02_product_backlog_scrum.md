# Product Backlog and Scrum

## 1. Purpose of This Document

This document explains how **Scrum** was applied to organise the AI Risk Detector project.

It combines:

- Product Backlog structure;
- Epics;
- User Stories;
- Acceptance Criteria;
- Priority Score;
- Story Points;
- Sprint allocation;
- Definition of Ready;
- Definition of Done;
- Jira alignment.

Jira was used as the Scrum management tool. The repository documents the rationale and structure of the project, while Jira provides the operational view of the backlog, sprints and workflow.

---

## 2. Scrum Approach

Scrum was used to organise the project into manageable work items and short delivery cycles.

The project used Scrum concepts to:

- define a Product Backlog;
- organise work into Epics and User Stories;
- prioritise backlog items;
- estimate effort using Story Points;
- allocate work into sprints;
- track progress through Jira;
- support incremental delivery of the MVP and documentation.

The project does not assign Scrum roles to specific people in the repository. Instead, Scrum responsibilities were applied at team level.

The team used Scrum to structure the work around a clear product goal:

> deliver a lightweight MVP that analyses software risks and generates backlog-ready user stories for Agile and DevOps teams.

---

## 3. Product Backlog

The **Product Backlog** is the ordered list of work needed to improve the product.

In this project, the Product Backlog includes:

- functional user stories;
- backlog refinement features;
- Scrum support features;
- DevOps and release readiness features;
- documentation and evidence tasks;
- future improvements.

The backlog was created to connect the product vision with actual delivery work in Jira.

Each backlog item includes:

- ID;
- Epic;
- User Story or Task;
- Acceptance Criteria;
- Priority Score;
- Story Points;
- Sprint allocation.

---

## 4. Priority Score

The project used a simplified Priority Score from 1 to 4.

| Priority Score | Meaning |
|---|---|
| 4 | Must Have / Critical for project evaluation |
| 3 | High value |
| 2 | Medium value |
| 1 | Low value / Future improvement |

Priority Score represents value and importance, not effort.

For example, a feature can have low priority but high effort if it is useful for the future but not required for the current MVP.

---

## 5. Story Points

Story Points were used to estimate effort and complexity.

| Story Points | Meaning |
|---|---|
| 1 | Very small |
| 2 | Small |
| 3 | Medium |
| 5 | Large |
| 8 | Too large, should probably be split |

Story Points are different from priority.

- Priority answers: **How important is this item?**
- Story Points answer: **How much effort or complexity does this item represent?**

---

## 6. Epics

The Jira backlog was organised using the following Epics.

| Epic | Description |
|---|---|
| EPIC 1 - Task Input and Risk Analysis | Features related to submitting a task, analysing it and producing a basic risk report |
| EPIC 2 - Backlog Quality and Acceptance Criteria | Features related to improving backlog items, user stories and acceptance criteria |
| EPIC 3 - Scrum Events Support | Features related to Sprint Planning, Sprint Review and Retrospective support |
| EPIC 4 - DevOps and Release Readiness | Features related to suggested tests, release readiness, rollback and deployment risk |
| EPIC 5 - Responsible AI and Documentation | Features and tasks related to human validation, documentation and project evidence |
| EPIC 6 - Future Integrations | Future improvements such as Jira integration, dashboards and analytics |

These Epics helped group related work and make the backlog easier to understand.

---

## 7. Product User Stories

The following user stories represent the main product backlog.

| ID | Epic | User Story | Acceptance Criteria | Priority | Story Points | Sprint |
|---|---|---|---|---|---|---|
| US01 | EPIC 1 | As a user, I want to enter a software task description, so that I can submit it for risk analysis. | Given I have a task description, when I enter it into the system, then the system accepts the input for analysis. | 4 | 2 | Sprint 1 |
| US02 | EPIC 1 | As a user, I want the system to analyse my task using AI-supported logic, so that I receive a structured risk assessment. | Given I submit a valid task, when the analysis is performed, then the system returns a structured risk report. | 4 | 3 | Sprint 1 |
| US03 | EPIC 1 | As a user, I want to see a risk level, so that I can quickly understand the severity of the task. | Given the task has been analysed, when the report is displayed, then the system shows a Low, Medium or High risk level. | 4 | 2 | Sprint 1 |
| US04 | EPIC 1 | As a user, I want to see potential risks, so that I can understand what could go wrong before execution. | Given the task has been analysed, when the report is generated, then the system lists relevant potential risks. | 4 | 3 | Sprint 1 |
| US05 | EPIC 1 | As a user, I want to see the estimated impact of the risks, so that I can understand the possible consequences. | Given risks are identified, when the report is displayed, then each relevant risk includes a short impact explanation. | 3 | 2 | Sprint 1 |
| US06 | EPIC 1 | As a user, I want to receive recommendations, so that I can reduce the identified risks before execution. | Given risks are identified, when the report is generated, then the system suggests practical mitigation actions. | 4 | 3 | Sprint 1 |
| US07 | EPIC 4 | As a user, I want to see suggested tests, so that I can validate the task before implementation or release. | Given a task has been analysed, when the report is generated, then the system suggests relevant tests or quality checks. | 4 | 3 | Sprint 2 |
| US08 | EPIC 2 | As a user, I want to see possible acceptance criteria, so that the task can become clearer and easier to validate. | Given a task or requirement is submitted, when the report is generated, then the system proposes concise acceptance criteria. | 4 | 3 | Sprint 2 |
| US09 | EPIC 2 | As a user, I want to receive suggestions to improve unclear tasks, so that the backlog item becomes more actionable. | Given an ambiguous task is submitted, when the analysis is generated, then the system suggests how to make the task clearer, smaller or more testable. | 3 | 3 | Sprint 2 |
| US10 | EPIC 3 | As a Scrum team member, I want the assistant to support Sprint Planning, so that the team can identify risks and preparation needs before selecting work. | Given a task is being considered for a sprint, when the assistant analyses it, then the output helps the team discuss risks, tests and acceptance criteria before planning. | 3 | 2 | Sprint 2 |
| US11 | EPIC 3 | As a Scrum team member, I want the assistant to support Sprint Review, so that the team can discuss whether the increment addressed relevant risks and quality concerns. | Given an increment is being reviewed, when the team compares the output with the initial risk analysis, then the team can discuss what was addressed and what remains open. | 2 | 2 | Sprint 3 |
| US12 | EPIC 3 | As a Scrum Master, I want the assistant to support Retrospective discussions, so that the team can identify recurring risks and improvement actions. | Given the team reviews previous tasks or risks, when the assistant is used in a retrospective context, then it suggests possible improvement actions. | 2 | 2 | Sprint 3 |
| US13 | EPIC 4 | As a DevOps team member, I want release readiness support, so that the team can identify deployment, rollback, monitoring or testing concerns before release. | Given a release-related task is submitted, when the report is generated, then the system identifies readiness concerns such as rollback, monitoring, testing or dependencies. | 4 | 3 | Sprint 3 |
| US14 | EPIC 5 | As a user, I want to copy or export the generated output, so that it can be added manually to Jira, documentation or sprint evidence. | Given a risk report has been generated, when I review the output, then I can copy the relevant content for use in Jira or project documentation. | 2 | 2 | Sprint 3 |
| US15 | EPIC 6 | As a Product Owner, I want future Jira integration, so that generated recommendations can be linked directly to backlog items. | Given a future version of the product, when a report is generated, then the output can be connected to a Jira issue. | 1 | 5 | Future |

---

## 8. Documentation and Project Tasks

In addition to product user stories, the backlog also included documentation and project evidence tasks.

| ID | Task | Acceptance Criteria | Priority | Story Points | Sprint |
|---|---|---|---|---|---|
| DOC01 | Rewrite README | Given the repository is opened, when the evaluator reads the README, then the project purpose and structure are clear. | 4 | 2 | Sprint 2 |
| DOC02 | Complete project overview | Given the overview document is opened, when it is read, then the project context and objective are clear. | 4 | 2 | Sprint 2 |
| DOC03 | Complete product backlog and Scrum document | Given the backlog document is reviewed, when the evaluator checks it, then all main user stories and acceptance criteria are visible. | 4 | 3 | Sprint 2 |
| DOC04 | Complete DevOps and MVP document | Given the DevOps document is opened, when it is read, then the MVP, tests and CI pipeline are explained. | 4 | 3 | Sprint 3 |
| DOC05 | Complete critical reflection | Given the reflection document is opened, when it is read, then the project includes a critical analysis of AI, Scrum and DevOps. | 4 | 4 | Sprint 3 |

These tasks were included because the assignment evaluates not only the MVP, but also the project management approach, DevOps evidence and critical reflection.

---

## 9. Sprint Allocation

The work was organised into three sprints.

| Sprint | Focus | Items |
|---|---|---|
| Sprint 1 | Core MVP risk analysis | US01, US02, US03, US04, US05, US06 |
| Sprint 2 | Backlog quality, suggested tests and Scrum support | US07, US08, US09, US10, DOC01, DOC02, DOC03 |
| Sprint 3 | Release readiness, final documentation and reflection | US11, US12, US13, US14, DOC04, DOC05 |
| Future | Future improvements | US15 |

This sprint allocation reflects an incremental approach.

The first sprint focused on the minimum usable risk analysis flow. Later sprints improved backlog quality, Scrum support, DevOps alignment and final documentation.

---

## 10. Jira Alignment

Jira was used as the Scrum management tool for the project.

The Jira board includes:

- Epics;
- User Stories;
- Acceptance Criteria;
- Priority information;
- Story Points;
- Sprint allocation;
- workflow status.

The Jira workflow used was:

`To Do -> In Progress -> In Review -> Done`

Jira made the work visible and helped connect the Product Backlog with sprint execution.

The Jira board is linked in the main `README.md`.

---

## 11. Definition of Ready

A backlog item was considered **Ready** when it had enough information to be selected for a sprint.

For this project, a backlog item was Ready when:

- the user story followed the format "As a..., I want..., so that...";
- the expected value was clear;
- acceptance criteria were defined;
- priority was assigned;
- story points were estimated;
- the related Epic was identified;
- dependencies or assumptions were understood;
- the team understood what had to be delivered.

The Definition of Ready helped reduce ambiguity before sprint work started.

---

## 12. Definition of Done

A backlog item was considered **Done** when it met the agreed quality and evidence expectations.

For this project, a backlog item was Done when:

- the acceptance criteria were satisfied;
- the Jira status was updated;
- the functionality or documentation was completed;
- tests passed when applicable;
- the output supported the MVP, Scrum evidence, DevOps evidence or final reflection;
- AI-generated suggestions were treated as decision support and not as automatic decisions.

The Definition of Done ensured that completion meant more than simply creating a file or writing code.

---

## 13. Scrum Reflection

Scrum helped the team organise an open and uncertain assignment into smaller, manageable pieces of work.

The project did not attempt to build a complete AI platform from the beginning. Instead, the work was structured around a backlog, prioritised user stories and incremental delivery.

This was important because the product idea evolved from a general AI assistant concept into a focused MVP that analyses risks and generates user stories.

Scrum also supported transparency through Jira and helped connect the product idea with concrete deliverables such as the MVP, tests, CI pipeline and documentation.

The main learning is that Scrum provides structure, but it does not guarantee quality by itself. Quality also required DevOps practices such as testing, version control and pipeline automation.