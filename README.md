# AI Risk Detector — DevOps AI Assistant ⚠️

## Agile Project Management — Group 5

AI Risk Detector is an AI-powered assistant designed to support software teams working in Agile, Scrum and DevOps environments.

The main goal of this project is not only to build a software application, but to demonstrate how Agile Project Management concepts can be applied in a real product context. The application acts as evidence of the concepts studied in the course: Product Backlog, User Stories, Sprint Planning, Sprint Review, Sprint Retrospective, DevOps practices, continuous feedback, quality management and risk mitigation.

---

## 1. Project Context

Software development teams working in Agile environments often face problems such as:

- Poorly structured backlog items.
- Ambiguous requirements.
- Lack of visibility about technical and delivery risks.
- Rework caused by late identification of problems.
- Difficulty preparing Sprint Planning, Sprint Review or Retrospective.
- Lack of standardised criteria to evaluate task or release readiness.
- Decisions based mainly on intuition rather than structured analysis.

In Agile and DevOps contexts, these problems can affect delivery speed, software quality and team confidence. If risks are discovered too late, they can lead to sprint failures, deployment issues, production incidents or delays.

AI Risk Detector addresses this problem by introducing an AI-supported step before task execution or release preparation.

---

## 2. Product Vision

The vision of AI Risk Detector is to help Agile software teams make better decisions before executing technical tasks, planning sprints or preparing releases.

The assistant receives a software task or requirement written in natural language and returns a structured analysis containing:

- Potential risks.
- Risk level classification.
- Estimated impact.
- Mitigation recommendations.
- Possible acceptance criteria.
- Suggested tests or quality checks.
- Suggestions to improve the task before execution.

The product is designed to support the team, not to replace it. The AI provides recommendations, but the final decision must always be validated by the Product Owner, Scrum Master, Developers or other stakeholders.

---

## 3. Problem Statement

Agile teams need to deliver value quickly, but fast delivery can create risk if requirements are unclear or technical tasks are not properly analysed.

Common examples include:

- A deployment task with no rollback plan.
- A user story without clear acceptance criteria.
- A backlog item that is too large for one sprint.
- A release with insufficient testing.
- A task that depends on external systems or APIs.
- A technical change that may affect production stability.

Without proactive risk identification, teams may only discover problems during testing, deployment or even after release. This increases rework and reduces trust in the delivery process.

---

## 4. Proposed Solution

AI Risk Detector is a lightweight web-based MVP that uses Artificial Intelligence to analyse software tasks and generate structured risk reports.

The user enters a task or requirement, for example:

> "Deploy the new authentication module to production"

The system analyses the input and returns:

- Risk level: High, Medium or Low.
- Potential risks.
- Estimated impact.
- Recommendations to reduce risk.
- Suggested tests.
- Possible acceptance criteria.
- Improvement suggestions for the backlog item.

This allows the team to discuss risks earlier, improve task quality and prepare better Sprint Planning or release decisions.

---

## 5. Relationship with Agile Concepts

This project is aligned with Agile because it focuses on:

### Iterative and Incremental Delivery

The product was developed as an MVP and can evolve through multiple sprints. Instead of trying to build a complete tool from the beginning, the first increment focuses on validating the core value: AI-based risk analysis.

### Customer Collaboration

The project is based on the idea that feedback from the client, professor or stakeholders should be used to refine the backlog and improve the product direction.

### Responding to Change

The backlog is not fixed. If feedback shows that a different functionality brings more value, the Product Backlog can be adapted.

### Working Software

The project includes a functional prototype, but the prototype is used as evidence of Agile and DevOps concepts rather than as the only objective of the assignment.

### Continuous Improvement

The assistant supports continuous improvement by helping teams identify risks, propose mitigations and reflect on quality before execution.

---

## 6. Scrum Applied to the Project

Scrum was used as the management framework for organising the work.

The project applies Scrum through:

- Product Backlog.
- User Stories.
- Acceptance Criteria.
- Prioritisation.
- Sprint Planning.
- Sprint Backlog.
- Sprint Review.
- Sprint Retrospective.
- Increment delivery.

Scrum helps the team structure the work, define priorities and deliver value progressively.

---

## 7. Scrum Roles in the Project

### Product Owner

The Product Owner is responsible for maximising product value. In this project, the Product Owner perspective is represented by the need to prioritise features that bring the highest value to Agile and DevOps teams.

Examples of Product Owner decisions:

- Prioritising risk analysis before advanced integrations.
- Defining which user stories belong to the MVP.
- Ensuring that the backlog reflects the problem described in the project statement.
- Deciding that Jira integration and user story generation are important next steps.

### Scrum Master

The Scrum Master is responsible for helping the team apply Scrum correctly.

In this project, the Scrum Master perspective is connected to:

- Facilitating Sprint Planning.
- Ensuring that the team understands the Sprint Goal.
- Supporting Sprint Review and Retrospective.
- Helping the team identify blockers.
- Promoting continuous improvement.

### Developers

The Developers are responsible for building the product increment.

In this project, Developers worked on:

- Application structure.
- AI integration.
- User interface.
- Risk analysis output.
- Documentation.
- Repository organisation.
- DevOps evidence.

---

## 8. Product Backlog

The Product Backlog is a prioritised list of everything that may be developed in the product.

The backlog includes functional features, quality improvements, DevOps practices and future integrations. It evolves based on feedback and learning.

| ID | User Story | Priority | Scrum/DevOps Concept |
|---|---|---|---|
| US1 | As a user, I want to enter a software task description, so that I can submit it for risk analysis. | High | Product Backlog / MVP |
| US2 | As a user, I want the system to analyse my task using AI, so that I receive a structured risk assessment. | High | AI-supported decision making |
| US3 | As a user, I want to see a risk level, so that I can quickly understand the severity of the task. | High | Quality / Risk Management |
| US4 | As a user, I want to see potential risks, so that I can understand what could go wrong before execution. | High | Shift-left risk detection |
| US5 | As a user, I want to see the estimated impact of each risk, so that I can prioritise mitigation actions. | High | Prioritisation |
| US6 | As a user, I want recommendations for each risk, so that I can reduce possible problems before delivery. | High | Continuous improvement |
| US7 | As a user, I want structured results, so that the output is easy to understand and discuss with the team. | Medium | Transparency |
| US8 | As a user, I want loading feedback, so that I know the system is processing the analysis. | Medium | User experience |
| US9 | As a user, I want clear error handling, so that I can recover from failed analysis attempts. | Medium | Reliability |
| US10 | As a user, I want to start a new analysis, so that I can evaluate multiple tasks in the same session. | Medium | Workflow support |
| US11 | As a user, I want a responsive interface, so that I can use the tool from different devices. | Medium | Accessibility |
| US12 | As a first-time user, I want an example task placeholder, so that I understand the expected input. | Low | Usability |
| US13 | As a user, I want to copy the results, so that I can share them with my team or include them in documentation. | Low | Collaboration |
| US14 | As a Product Owner, I want the assistant to generate user stories from ambiguous requirements, so that the backlog becomes clearer and easier to prioritise. | High | Backlog refinement |
| US15 | As a Product Owner, I want the assistant to generate acceptance criteria, so that the team has a shared definition of what must be delivered. | High | Acceptance criteria / Sprint Planning |
| US16 | As a Scrum Master, I want the assistant to suggest questions for Sprint Retrospective, so that the team can identify process improvements. | Medium | Retrospective / Continuous improvement |
| US17 | As a DevOps team member, I want the assistant to suggest tests for a task, so that quality is considered before deployment. | High | Continuous Testing |
| US18 | As a release responsible, I want the assistant to evaluate release readiness, so that the team can decide whether a deployment is safe. | High | Release readiness / DevOps |
| US19 | As a team member, I want to export generated user stories to a Jira-compatible format, so that they can be added to the Product Backlog. | High | Scrum tool integration |
| US20 | As a team member, I want Jira integration through API in the future, so that generated backlog items can be created directly as Jira issues. | Medium | Automation / DevOps |

---

## 9. Sprint 1 Scope

Sprint 1 focused on validating the core product concept.

### Sprint Goal

Deliver a first functional MVP capable of receiving a software task and returning an AI-generated risk analysis.

### Sprint 1 Selected Backlog Items

The first sprint focused mainly on:

- Task input interface.
- AI-powered risk analysis.
- Risk level display.
- Potential risks list.
- Impact description.
- Recommendations display.
- Structured results view.

### Sprint 1 Increment

The Sprint 1 increment is a functional prototype where the user can enter a software task and receive a structured risk report.

This increment validates the main assumption of the project: AI can support Agile and DevOps teams by identifying possible risks before task execution.

---

## 10. Sprint Planning Applied

Sprint Planning was used to define what should be delivered in Sprint 1.

During Sprint Planning, the team selected backlog items that were essential for the MVP. The focus was not to build every possible feature, but to deliver the minimum useful increment that demonstrates the concept.

The selected scope answered the question:

> What is the smallest product increment that proves the value of AI-supported risk analysis?

The answer was:

> A working interface where a user submits a task and receives risks, impact and recommendations.

---

## 11. Sprint Review Applied

Sprint Review is used to inspect the product increment and collect feedback.

For this project, the Sprint Review focuses on showing:

- The task input interface.
- The AI-generated risk analysis.
- The risk level classification.
- The recommendations.
- How the output could support backlog refinement, Sprint Planning or release decisions.

Feedback from Sprint Review should be used to update the Product Backlog.

Possible feedback examples:

- The tool should also generate user stories.
- The output should be exportable to Jira.
- The risk analysis should include suggested tests.
- The tool should support release readiness decisions.

---

## 12. Sprint Retrospective Applied

Sprint Retrospective focuses on how the team worked, not only on what was built.

In this project, the retrospective can be used to reflect on:

### What went well

- The team defined a clear MVP.
- The backlog was structured using user stories.
- The project connected Scrum, DevOps and AI.
- The repository was organised into source code, documentation and management evidence.

### What could be improved

- The connection between the software and the theoretical concepts should be made more explicit.
- Jira integration should be added or better documented.
- More tests and pipeline evidence should be included.
- The AI output should be validated with clearer criteria.

### Improvement actions

- Add user story generation functionality.
- Add Jira-compatible export.
- Add tests for core features.
- Improve DevOps evidence.
- Add a stronger critical reflection on AI limitations.

---

## 13. DevOps Applied to the Project

DevOps is applied in two ways:

1. As part of the team delivery process.
2. As part of the product value proposition.

### 13.1 DevOps in the Delivery Process

The project applies basic DevOps principles through:

- Centralised GitHub repository.
- Version control.
- Structured project folders.
- Dependency management through `requirements.txt`.
- Separation between source code, documentation, management and presentation materials.
- Possibility of automated testing.
- Possibility of CI/CD pipeline.
- MVP delivery mindset.
- Continuous improvement based on feedback.

### 13.2 DevOps in the Product Itself

AI Risk Detector supports DevOps teams by helping with:

- Early risk identification.
- Shift-left quality.
- Suggested tests.
- Release readiness analysis.
- Mitigation recommendations.
- Continuous feedback.
- Reduction of rework.
- Better visibility before deployment.

---

## 14. AI Risk Detector in the DevOps Lifecycle

The tool can be mapped to the DevOps lifecycle:

### Plan

The assistant helps analyse tasks, requirements and backlog items before execution.

Example:

- Detecting ambiguous requirements.
- Suggesting user stories.
- Suggesting acceptance criteria.
- Supporting Sprint Planning.

### Build

The assistant helps identify technical risks before development starts.

Example:

- Dependencies.
- Integration risks.
- Complexity.
- Security concerns.

### Test

The assistant can suggest tests and validation criteria.

Example:

- Unit tests.
- Integration tests.
- Regression tests.
- User acceptance tests.

### Release

The assistant can support release readiness by identifying risks before deployment.

Example:

- Missing rollback plan.
- Insufficient monitoring.
- High-impact changes.
- Incomplete testing.

### Deploy

The assistant can help the team think about deployment risks.

Example:

- Production impact.
- Downtime.
- Infrastructure dependencies.
- Configuration errors.

### Operate

Future versions could use incidents and monitoring data to improve risk predictions.

Example:

- Learning from previous incidents.
- Analysing post-release problems.
- Supporting operational decisions.

### Monitor

The tool could be extended to monitor usage, quality of AI responses and recurring risks.

Example:

- Most common risk categories.
- Number of high-risk tasks.
- Accepted vs rejected recommendations.
- Feedback from users.

---

## 15. Jira Integration and Backlog Management

A relevant improvement requested for this project is the ability to generate user stories and move them into Jira or a Jira-compatible backlog.

This is important because Jira is commonly used as a Scrum management tool for:

- Product Backlog.
- Sprint Backlog.
- User Stories.
- Tasks.
- Bugs.
- Sprint Planning.
- Sprint Review evidence.

### Proposed Jira-Compatible Output

The assistant should be able to generate:

- Issue type: Story, Task or Bug.
- Summary.
- Description.
- User story format.
- Acceptance criteria.
- Priority.
- Risk level.
- Suggested sprint.
- Labels.
- Mitigation recommendations.

### Example Jira-ready User Story

**Issue Type:** Story  
**Summary:** Generate risk analysis from a software task  
**Description:** As a user, I want the assistant to analyse a software task, so that I can identify risks before execution.  
**Acceptance Criteria:**

- The user can enter a task description.
- The system returns a risk level.
- The system lists potential risks.
- The system provides impact and recommendations.
- The output is displayed in a structured format.

**Priority:** High  
**Labels:** AI, DevOps, Risk, Scrum  
**Risk Level:** Medium  

### Implementation Options

There are two possible approaches:

1. Export generated user stories to CSV, allowing manual import into Jira.
2. Integrate with the Jira API in a future sprint, allowing automatic issue creation.

For the current academic project, a Jira-compatible structure or export is enough to demonstrate the conceptual connection between AI, Product Backlog and Scrum. A complete API integration can be considered a future improvement.

---

## 16. Artificial Intelligence Role

Artificial Intelligence is used as a support mechanism for Agile and DevOps decision-making.

The AI helps with:

- Analysing ambiguous software tasks.
- Identifying possible risks.
- Classifying risk severity.
- Suggesting mitigations.
- Suggesting tests.
- Supporting backlog refinement.
- Supporting release readiness.
- Reducing manual analysis effort.

However, AI does not replace human judgement. The output must be reviewed by the team.

The Product Owner, Scrum Master and Developers remain responsible for validating whether the AI recommendations are useful, realistic and aligned with the product goals.

---

## 17. AI Limitations and Critical Reflection

Using AI in Agile and DevOps contexts introduces risks and limitations.

### Main limitations

- The AI may generate incomplete or incorrect recommendations.
- The quality of the output depends on the quality of the input.
- Ambiguous tasks may lead to generic answers.
- The AI may not understand the full technical or business context.
- The AI can create false confidence if its output is accepted without review.
- Sensitive data should not be submitted without privacy controls.
- Human validation is always required.

### Critical Reflection

The value of AI Risk Detector is not that it automatically makes decisions for the team. Its value is that it supports discussion, makes risks more visible and helps the team think earlier about quality, testing and delivery.

This aligns with Agile and DevOps because both approaches value feedback, transparency, collaboration and continuous improvement.

---

## 18. Quality and Risk Management

AI Risk Detector supports quality management by moving risk analysis earlier in the development lifecycle.

This is connected to the DevOps idea of shift-left practices: quality should not be checked only at the end of the process, but continuously from the beginning.

The tool helps teams ask questions such as:

- Is this task clear enough?
- What could go wrong?
- What is the impact if it fails?
- What tests should be created?
- Is the task ready for development?
- Is the release ready for deployment?
- What mitigation actions should be taken?

By answering these questions earlier, the team can reduce rework and improve delivery confidence.

---

## 19. Main Features

### Implemented in Sprint 1

- Task input interface.
- AI-powered risk analysis.
- Risk level classification.
- Potential risks list.
- Impact description.
- Mitigation recommendations.
- Structured output view.
- Basic MVP interface.

### Planned or Recommended Improvements

- Automatic user story generation.
- Acceptance criteria generation.
- Jira-compatible export.
- Jira API integration.
- Suggested tests.
- Release readiness score.
- Risk history.
- Feedback collection.
- Automated tests.
- CI/CD pipeline.
- Monitoring dashboard.
- Improved prompt engineering.
- Validation metrics for AI output quality.

---

## 20. Repository Structure

The repository is organised to separate source code, documentation and project management evidence.

```text
/
├── docs/              # Technical documentation and sprint reflections
├── management/        # Scrum evidence: backlog, sprint planning, boards
├── presentation/      # Presentation materials
├── src/               # Application source code
├── README.md          # Project overview and conceptual explanation
└── requirements.txt   # Python dependencies
