# DevOps and MVP

## 1. Purpose of This Document

This document explains how the AI Risk Detector MVP was implemented and how DevOps concepts were applied in the project.

It covers:

- MVP description;
- main user flow;
- application features;
- rule-based AI prototype approach;
- local execution;
- testing strategy;
- GitHub Actions CI pipeline;
- DevOps evidence;
- limitations;
- future improvements.

The goal is to show that the project includes not only a working prototype, but also basic delivery, testing and quality practices aligned with DevOps.

---

## 2. MVP Description

The MVP is a Streamlit application that supports Agile and DevOps teams before implementation or release.

The user enters a software task, requirement or idea. The app then produces two main outputs:

1. **Risk Analysis**
2. **Generated User Story**

The MVP demonstrates the core product value:

> helping teams identify risks earlier, improve backlog quality and prepare better user stories before work starts.

The application is intentionally lightweight. It focuses on the main value of the product rather than advanced technical features.

---

## 3. Main User Flow

The main user flow is simple:

1. The user opens the Streamlit app.
2. The user enters a task, requirement or idea.
3. The user clicks the analysis button.
4. The app analyses the input using rule-based logic.
5. The app returns a structured risk analysis.
6. The app generates a user story with acceptance criteria.
7. The team can use the output to support Scrum planning, backlog refinement or release readiness discussion.

Example input:

`Deploy the new authentication module to production without a rollback plan.`

Expected output includes:

- High risk level;
- production and authentication risks;
- missing rollback concern;
- suggested tests;
- mitigation actions;
- release readiness notes;
- generated user story;
- Given / When / Then acceptance criteria.

---

## 4. Application Features

The MVP includes the following features.

| Feature | Description |
|---|---|
| Task input | User enters a software task, requirement or idea |
| Risk Level | Classifies the task as Low, Medium or High risk |
| Risk Score | Provides a numeric score from 1 to 10 |
| Potential Risks | Lists possible technical, delivery or release risks |
| Estimated Impact | Explains the possible consequences of the risks |
| Mitigation Recommendations | Suggests actions to reduce risk |
| Suggested Tests | Recommends relevant tests or quality checks |
| Release Readiness Notes | Indicates whether the task appears ready for release |
| Backlog Improvement Suggestions | Suggests how to improve unclear work items |
| Generated User Story | Converts the task into a backlog-ready user story |
| Acceptance Criteria | Generates Given / When / Then acceptance criteria |
| Priority and Story Points | Suggests priority and effort estimates |
| Suggested Epic | Links the item to a product or project area |
| Definition of Ready Checklist | Helps assess whether the item is ready for sprint planning |
| Human Validation Note | Reminds users that final decisions require human review |

---

## 5. Rule-Based AI Prototype Approach

The MVP does not use a real external AI API.

Instead, it uses deterministic rule-based logic to simulate how an AI-supported assistant could support risk analysis and user story generation.

The app analyses keywords such as:

- production;
- deployment;
- authentication;
- database;
- migration;
- payment;
- security;
- rollback;
- testing;
- API;
- integration;
- monitoring.

Based on these keywords, the app generates structured recommendations.

This approach was chosen for three reasons:

1. **Simplicity** - the app can run locally without external services.
2. **Reproducibility** - the same input produces the same output.
3. **Academic focus** - the main goal is to demonstrate Agile, Scrum and DevOps practices, not to build a production AI platform.

In a real product, the rule-based logic could be extended with a Large Language Model, but only with appropriate validation, monitoring and responsible AI controls.

