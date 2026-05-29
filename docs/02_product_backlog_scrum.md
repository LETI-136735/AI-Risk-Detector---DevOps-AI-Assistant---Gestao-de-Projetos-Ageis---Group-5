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

The team used Scrum to structure the work around a clear product goal:

> Deliver a lightweight MVP that analyses software risks and generates backlog-ready user stories for Agile and DevOps teams.

---

## 3. Product Backlog

The Product Backlog contains all work required to improve the product.

Each backlog item includes:

- ID;
- Epic;
- User Story;
- Acceptance Criteria;
- Sprint allocation.

---

## 4. Priority Score

| Priority Score | Meaning |
|---|---|
| 4 | Must Have |
| 3 | High Value |
| 2 | Medium Value |
| 1 | Future Improvement |

---

## 5. Story Points

| Story Points | Meaning |
|---|---|
| 1 | Very Small |
| 2 | Small |
| 3 | Medium |
| 5 | Large |
| 8 | Too Large |

---

## 6. Epics

| Epic | Description |
|---|---|
| EPIC 1 – Core Risk Analysis | Task submission, risk analysis, impact estimation and recommendations |
| EPIC 2 – Risk Visualization | Risk level display, potential risks and structured presentation of results |
| EPIC 3 – Backlog Intelligence | User story generation and acceptance criteria generation |
| EPIC 4 – DevOps and Release Readiness | Test suggestions and release readiness evaluation |
| EPIC 5 – Platform Usability | Loading feedback, error handling, responsive UI and usability improvements |
| EPIC 6 – Integrations | Jira export and future Jira API integration |
| EPIC 7 – Agile Process Support | Retrospective support for Scrum teams |

---

## 7. Product User Stories

### Sprint 1 – Must Have (MVP)

| ID | Epic | User Story |
|---|---|---|
| US1 | EPIC 1 | Submit Task Description |
| US2 | EPIC 1 | AI Risk Analysis |
| US3 | EPIC 2 | Risk Level Display |
| US4 | EPIC 2 | Potential Risks Display |
| US5 | EPIC 1 | Risk Impact Estimation |
| US6 | EPIC 1 | Risk Recommendations |
| US14 | EPIC 3 | Generate User Stories from Requirements |
| US15 | EPIC 3 | Generate Acceptance Criteria |

### Sprint 2 – Should Have

| ID | Epic | User Story |
|---|---|---|
| US7 | EPIC 2 | Structured Results |
| US8 | EPIC 5 | Loading Feedback |
| US9 | EPIC 5 | Error Handling |
| US10 | EPIC 5 | New Analysis |
| US11 | EPIC 5 | Responsive Interface |
| US17 | EPIC 4 | Test Suggestions |
| US18 | EPIC 4 | Release Readiness Evaluation |
| US19 | EPIC 6 | Jira Export |

### Sprint 3 – Could Have

| ID | Epic | User Story |
|---|---|---|
| US12 | EPIC 5 | First-Time User Placeholder |
| US13 | EPIC 5 | Copy Results |
| US16 | EPIC 7 | Retrospective Questions |
| US20 | EPIC 6 | Jira API Integration |

---

## 8. Documentation and Project Tasks

Documentation tasks include README updates, project overview, Scrum evidence, DevOps evidence and critical reflection.

---

## 9. Sprint Allocation

| Sprint | Focus | Items |
|---|---|---|
| Sprint 1 – Must Have | Core Risk Analysis, Risk Visualization and Backlog Intelligence | US1, US2, US3, US4, US5, US6, US14, US15 |
| Sprint 2 – Should Have | Platform Usability, Structured Results, DevOps Support and Jira Export | US7, US8, US9, US10, US11, US17, US18, US19 |
| Sprint 3 – Could Have | Agile Support, Additional Usability and Future Integrations | US12, US13, US16, US20 |

---

## 10. Jira Alignment

The Jira workflow used was:

`To Do -> In Progress -> In Review -> Done`

Jira was the single source of truth for backlog management, sprint allocation and progress tracking.

---

## 11. Definition of Ready

A backlog item was Ready when:

- the user story was defined;
- acceptance criteria existed;
- the Epic was identified;
- dependencies were understood;
- the team understood the expected outcome.

---

## 12. Definition of Done

A backlog item was Done when:

- acceptance criteria were satisfied;
- implementation or documentation was completed;
- tests passed where applicable;
- Jira status was updated;
- the output supported MVP objectives.

---

## 13. Scrum Reflection

Scrum helped transform a broad project idea into manageable work items organised through Epics, User Stories and Sprints.

The combination of Scrum practices, Jira tracking, automated testing and CI/CD support allowed the project to demonstrate both Agile and DevOps principles.
