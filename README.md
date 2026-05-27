# AI Risk Detector — DevOps AI Assistant

**Agile Project Management — Group 5**

AI Risk Detector is an AI-supported assistant designed to help Agile and DevOps software teams identify risks, improve backlog quality and support better planning, testing and release readiness decisions.

This project was developed in the context of the **Agile Project Management** course. The main objective is not to build a complex production-ready software platform, but to demonstrate how **Agile, Scrum, DevOps and responsible AI concepts** can be applied in a realistic product context.

---

## 1. Project Summary

Software teams working in Agile and DevOps environments often need to deliver value quickly while managing uncertainty, technical complexity and changing requirements.

However, teams may face problems such as:

- poorly structured backlog items;
- ambiguous requirements;
- missing or weak acceptance criteria;
- insufficient test planning;
- low visibility of delivery and release risks;
- rework caused by late identification of problems;
- uncertainty about whether a task or release is ready to proceed.

**AI Risk Detector** addresses these problems by providing an AI-supported analysis of software tasks, user stories or requirements before execution.

The assistant receives a task or requirement written in natural language and returns a structured analysis including:

- risk level;
- potential risks;
- expected impact;
- mitigation recommendations;
- suggested tests;
- possible acceptance criteria;
- improvement suggestions for the backlog item.

The AI output is intended to support team discussion and decision-making. It does not replace the responsibility of the Product Owner, Scrum Master, Developers or other stakeholders.

---

## 2. Problem Context

In Agile environments, speed is important, but speed without clarity can create risk.

A team may start working on a user story or technical task that is not ready, too ambiguous or poorly analysed. This can lead to misunderstandings, sprint delays, incomplete increments, failed deployments or additional rework.

Examples of risky situations include:

- a deployment task without a rollback plan;
- a user story without clear acceptance criteria;
- a backlog item that is too large for one sprint;
- a release with insufficient testing;
- a requirement with hidden dependencies;
- a technical change that may affect production stability.

The project explores how AI can be used to support earlier risk identification and improve the quality of planning conversations in Agile and DevOps teams.

---

## 3. Proposed Solution

AI Risk Detector is a lightweight MVP that helps teams analyse software work items before implementation or release.

The user enters a task, requirement or user story, for example:

> "Deploy the new authentication module to production without a rollback plan."

The system then generates a structured risk report, such as:

- **Risk Level:** High
- **Potential Risks:** production outage, authentication failure, lack of rollback strategy
- **Impact:** users may be unable to log in if the deployment fails
- **Recommendations:** define a rollback plan, validate authentication flows, monitor login errors
- **Suggested Tests:** regression tests, authentication tests, rollback validation
- **Possible Acceptance Criteria:** rollback plan exists, monitoring is configured, deployment is approved

This output can be used during backlog refinement, Sprint Planning, Sprint Review, release preparation or retrospective discussions.

---

## 4. Alignment with Agile, Scrum and DevOps

This project is structured around three main areas: **Agile mindset**, **Scrum management** and **DevOps delivery practices**.

### Agile Alignment

The project follows Agile principles by focusing on:

- delivering a small but useful MVP;
- responding to feedback;
- improving the backlog iteratively;
- supporting collaboration between team members;
- prioritising working value over excessive documentation.

The AI assistant is not intended to create bureaucracy. Its purpose is to improve clarity, feedback and team learning.

### Scrum Alignment

Scrum is used as the project management framework.

The repository documents:

- Product Backlog;
- user stories;
- acceptance criteria;
- Sprint Planning;
- Sprint Review;
- Sprint Retrospective;
- Definition of Ready;
- Definition of Done;
- product increment and MVP scope.

Jira is used as the Scrum management tool to organise backlog items, sprint execution and workflow visibility.

### DevOps Alignment

DevOps is addressed both as a delivery approach and as part of the product concept.

The project connects with DevOps through:

- repository organisation;
- version control;
- documentation of delivery evidence;
- testing and quality considerations;
- release readiness analysis;
- feedback loops between planning, implementation and improvement.

The product itself also supports DevOps teams by helping identify delivery risks, suggest tests and improve release preparation.

---

## 5. MVP Scope

The MVP is intentionally lightweight.

The goal is to demonstrate the core value of the product: analysing a software task or requirement and producing a structured risk report that can support Agile and DevOps decisions.

### In Scope

The MVP focuses on:

- entering a software task or requirement;
- generating a risk level;
- identifying potential risks;
- explaining possible impact;
- suggesting mitigation actions;
- suggesting tests;
- proposing possible acceptance criteria;
- improving backlog item clarity.

### Out of Scope

The project does not aim to deliver:

- a production-ready enterprise AI platform;
- full Jira API integration;
- real-time production monitoring;
- a complete DevOps platform;
- an advanced AI governance system;
- a fully automated release management tool.

These elements are considered possible future improvements.

---

## 6. Repository Structure

```text
AI-Risk-Detector/
│
├── README.md
│
├── docs/
│   ├── 01_project_overview.md
│   ├── 02_product_vision.md
│   ├── 03_product_backlog.md
│   ├── 04_scrum_approach.md
│   ├── 05_devops_approach.md
│   ├── 06_mvp_description.md
│   ├── 07_responsible_ai_use.md
│   └── 08_final_report_draft.md
│
├── management/
│   ├── jira_board_evidence.md
│   ├── sprint_1_planning.md
│   ├── sprint_1_review.md
│   ├── sprint_1_retrospective.md
│   ├── sprint_2_planning.md
│   ├── sprint_2_review.md
│   └── sprint_2_retrospective.md
│
├── src/
│   └── application files
│
├── tests/
│   └── test files
│
└── .github/
    └── workflows/
```

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
