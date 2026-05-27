# Product Backlog

## 1. Purpose of the Product Backlog

The Product Backlog is the central artifact used to organise the product work of **AI Risk Detector**.

It connects the product vision with Scrum execution by translating the problem, target users and expected value into prioritised user stories.

In this project, the Product Backlog is used to:

- define the main product needs;
- prioritise the most valuable features;
- clarify the MVP scope;
- support Sprint Planning;
- provide input for Jira issues;
- document acceptance criteria;
- connect the product idea with Agile, Scrum and DevOps concepts.

The backlog is not fixed. It can evolve based on feedback from the professor, stakeholders, Sprint Review outcomes and team reflection.

---

## 2. Prioritisation Criteria

The Product Backlog was prioritised using the following criteria:

| Criteria | Explanation |
|---|---|
| User value | How useful the item is for Agile, Scrum or DevOps teams |
| Assignment alignment | How directly the item supports the academic project requirements |
| MVP contribution | Whether the item is necessary to demonstrate the core product concept |
| Risk reduction | Whether the item helps identify or reduce delivery, quality or release risks |
| Feasibility | Whether the item can realistically be addressed within the course scope |
| Learning value | Whether the item helps demonstrate Agile Project Management concepts |

High-priority items are those required to demonstrate the MVP and the core value of AI Risk Detector.

Medium-priority items improve the usefulness of the assistant and support stronger Scrum or DevOps alignment.

Low-priority items are valuable future improvements but are not essential for the current academic MVP.

---

## 3. MVP Definition

The MVP focuses on the simplest version of the product that demonstrates meaningful value.

The MVP allows a user to enter a software task, requirement or user story and receive a structured AI-supported risk report.

The report should include:

- risk level;
- potential risks;
- impact explanation;
- mitigation recommendations;
- suggested tests;
- possible acceptance criteria;
- improvement suggestions.

The MVP does not aim to provide full automation, enterprise integrations or production-grade AI governance. Its purpose is to validate the product idea and demonstrate how Agile, Scrum and DevOps concepts can be applied in a realistic project.

---

## 4. Product Backlog User Stories

| ID | Epic | User Story | Priority | Acceptance Criteria | Scrum/DevOps Value | MVP | Status |
|---|---|---|---|---|---|---|---|
| US01 | Task Input | As a software team member, I want to enter a task, requirement or user story, so that I can submit it for risk analysis. | High | Given I have a task or requirement, when I enter it into the assistant, then the system accepts the input for analysis. | Enables backlog refinement and Sprint Planning discussion. | Yes | To Do |
| US02 | Risk Analysis | As a software team member, I want the assistant to analyse my input, so that I can understand possible risks before execution. | High | Given I submit a valid task, when the analysis is performed, then the system returns a structured risk report. | Supports early risk identification and improves planning quality. | Yes | To Do |
| US03 | Risk Classification | As a Product Owner or Developer, I want to see a risk level, so that I can quickly understand the severity of the task. | High | Given a task has been analysed, when the report is displayed, then the system shows a Low, Medium or High risk level. | Helps prioritisation and decision-making during Sprint Planning. | Yes | To Do |
| US04 | Potential Risks | As a Developer, I want to see potential risks, so that I can understand what could go wrong before implementation. | High | Given a task has been analysed, when the report is generated, then the system lists relevant potential risks. | Supports shift-left risk detection and technical discussion. | Yes | To Do |
| US05 | Impact Explanation | As a Scrum team member, I want to understand the possible impact of a risk, so that the team can evaluate its importance. | High | Given risks are identified, when the report is displayed, then each relevant risk includes a short impact explanation. | Improves shared understanding and supports informed decisions. | Yes | To Do |
| US06 | Mitigation Recommendations | As a DevOps-oriented team member, I want mitigation recommendations, so that the team can reduce delivery or release risks. | High | Given risks are identified, when the report is generated, then the system suggests practical mitigation actions. | Connects risk analysis with continuous improvement and delivery reliability. | Yes | To Do |
| US07 | Suggested Tests | As a QA or Developer, I want suggested tests, so that the team can validate the task more effectively. | High | Given a task has been analysed, when the report is displayed, then the system suggests relevant tests or quality checks. | Supports continuous testing and quality improvement. | Yes | To Do |
| US08 | Acceptance Criteria Suggestions | As a Product Owner, I want possible acceptance criteria, so that unclear backlog items can be improved before the sprint. | High | Given a task or user story is submitted, when the report is generated, then the system proposes concise acceptance criteria. | Improves Product Backlog quality and Definition of Ready. | Yes | To Do |
| US09 | Backlog Item Improvement | As a Scrum Master, I want the assistant to suggest improvements to unclear backlog items, so that the team can reduce ambiguity. | Medium | Given an ambiguous work item is submitted, when the system analyses it, then it suggests how to make the item clearer and more actionable. | Supports backlog refinement and reduces sprint execution problems. | Yes | To Do |
| US10 | User Story Reformulation | As a Product Owner, I want the assistant to reformulate ambiguous requirements into better user stories, so that the backlog is easier to understand. | Medium | Given a vague requirement, when the assistant analyses it, then it proposes a user story using the format “As a..., I want..., so that...”. | Strengthens Scrum backlog management and user story quality. | No | To Do |
| US11 | Release Readiness Support | As a DevOps team member, I want the assistant to identify release readiness concerns, so that the team can prepare safer deployments. | Medium | Given a release-related task is submitted, when the report is generated, then the system identifies readiness concerns such as rollback, monitoring or testing. | Supports DevOps release preparation and risk mitigation. | No | To Do |
| US12 | Jira Copy Support | As a team member, I want to copy the generated output, so that it can be manually added to Jira issues or documentation. | Medium | Given a report has been generated, when I review the output, then I can copy the relevant text for use in Jira or project documents. | Connects MVP output with Scrum management evidence. | No | To Do |
| US13 | Retrospective Improvement Suggestions | As a Scrum Master, I want the assistant to suggest improvement actions, so that the team can use risk patterns in retrospectives. | Low | Given previous risks or issues are discussed, when the assistant is used in a retrospective context, then it suggests possible improvement actions. | Supports continuous improvement and Sprint Retrospective learning. | No | To Do |
| US14 | Responsible AI Disclaimer | As a stakeholder, I want the system to show that AI output requires human validation, so that users do not treat recommendations as automatic decisions. | High | Given the assistant generates a report, when the output is displayed, then it includes a clear note that final decisions require human validation. | Reinforces responsible AI use and human accountability. | Yes | To Do |
| US15 | Future Integration with Jira | As a Product Owner, I want future integration with Jira, so that generated recommendations can be attached directly to backlog items. | Low | Given a future version of the product, when the assistant generates a report, then the output can be connected to a Jira issue. | Future improvement for stronger Scrum tool integration. | No | Future |

---

## 5. MVP Backlog Selection

The MVP includes the backlog items required to demonstrate the core value of AI Risk Detector.

The selected MVP items are:

| ID | Reason for MVP Selection |
|---|---|
| US01 | The user must be able to submit a task or requirement. |
| US02 | Risk analysis is the central feature of the product. |
| US03 | Risk classification provides a quick and understandable result. |
| US04 | Potential risks explain what could go wrong. |
| US05 | Impact explanation helps the team understand the importance of each risk. |
| US06 | Mitigation recommendations connect analysis with action. |
| US07 | Suggested tests support quality and DevOps thinking. |
| US08 | Acceptance criteria suggestions improve backlog quality. |
| US09 | Backlog improvement suggestions reduce ambiguity. |
| US14 | Responsible AI disclaimer reinforces human validation and accountability. |

These items are enough to demonstrate a meaningful functional prototype without increasing the technical complexity beyond the academic purpose of the project.

---

## 6. Future Improvements

The following backlog items are considered future improvements:

| Improvement | Description |
|---|---|
| Jira API integration | Automatically send generated recommendations to Jira issues. |
| Historical risk analytics | Analyse repeated risks across multiple sprints or releases. |
| Team dashboard | Provide visual summaries of common risk areas. |
| Pipeline integration | Connect risk analysis with CI/CD pipeline results. |
| Monitoring integration | Use production monitoring data to improve future risk recommendations. |
| Advanced AI governance | Add stronger traceability, auditability and validation mechanisms. |
| Release readiness score | Generate a more advanced readiness score based on tests, risk and deployment criteria. |

These features would make the product more complete, but they are not necessary for the current MVP.

---

## 7. Relationship with Scrum and Jira

The Product Backlog documented here provides the basis for the Jira Scrum board.

Each user story can be converted into a Jira issue and organised into sprints according to priority and MVP relevance.

The relationship between this document and Jira is:

- this document explains the backlog rationale and academic structure;
- Jira provides operational evidence of Scrum execution;
- Sprint Planning selects items from this backlog;
- Sprint Review validates the increment;
- Sprint Retrospective identifies improvement actions;
- the backlog may be adapted based on feedback.

This ensures that the repository and Jira board are aligned.

---

## 8. Backlog Reflection

The Product Backlog demonstrates how the project translates a broad problem into manageable work items.

The highest-priority stories focus on the minimum value needed to validate the product: task input, risk analysis, risk classification, suggested tests, acceptance criteria and responsible AI use.

This prioritisation reflects an Agile approach because it avoids trying to build everything at once. Instead, the team focuses on delivering a small but valuable increment that can be reviewed, discussed and improved.

The backlog also reflects DevOps thinking because several stories focus on quality, testing, release readiness, risk mitigation and feedback loops.

Overall, the Product Backlog connects the product idea with Scrum execution and DevOps reasoning.
'