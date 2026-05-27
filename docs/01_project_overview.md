# Project Overview

## 1. Course Context

This project was developed for the **Agile Project Management** course.

The assignment focuses on designing a digital solution with an AI component to support software teams in activities related to planning, execution, quality, delivery and continuous improvement.

The project applies three main concepts from the course:

| Concept | Application in this project |
|---|---|
| Agile | Focus on a lightweight MVP, iterative improvement and response to feedback |
| Scrum | Product Backlog, user stories, acceptance criteria, sprint allocation and Jira board |
| DevOps | Repository, automated tests, CI pipeline, release readiness and quality feedback |

The objective is not only to build an application, but to demonstrate how Agile Project Management concepts can be applied in a realistic product scenario.

---

## 2. Project Summary

**AI Risk Detector** is an AI-supported MVP designed to help Agile and DevOps software teams analyse a task, requirement or idea before implementation or release.

The application receives a short description written by the user and generates:

- a risk analysis;
- a risk level and risk score;
- potential risks;
- estimated impact;
- mitigation recommendations;
- suggested tests;
- release readiness notes;
- backlog improvement suggestions;
- a generated user story;
- acceptance criteria in Given / When / Then format;
- suggested priority, story points and epic.

The goal is to support better planning conversations and improve the quality of backlog items before the team starts implementation.

---

## 3. Problem Statement

Agile teams often need to deliver value quickly. However, speed can create problems when the work entering a sprint is unclear, incomplete or poorly analysed.

Common problems include:

- vague or ambiguous requirements;
- poorly structured backlog items;
- missing acceptance criteria;
- lack of testing expectations;
- weak visibility of delivery or technical risks;
- unclear release readiness;
- missing rollback or monitoring considerations;
- rework caused by late discovery of problems.

For example, a team may plan a deployment to production without a rollback plan or without enough testing. The problem may only become visible during release, when the cost of fixing it is much higher.

AI Risk Detector addresses this by helping the team identify possible risks earlier and transform vague tasks into more structured backlog items.

---

## 4. Product Vision

The vision of AI Risk Detector is to support Agile and DevOps teams in making better decisions before starting implementation or release activities.

The product helps teams move from unclear work items to more structured and actionable backlog items.

A concise product vision statement is:

> AI Risk Detector helps Agile and DevOps teams identify risks, improve backlog quality and prepare safer releases by analysing tasks and generating structured user stories, acceptance criteria and testing suggestions.

---

## 5. Target Users

The product is designed for software teams working in Agile and DevOps contexts.

The main target users are:

| User | How the product helps |
|---|---|
| Product Owner | Improves backlog clarity and acceptance criteria |
| Scrum Master | Supports planning, risk visibility and continuous improvement |
| Developers | Identifies technical risks and suggested tests before implementation |
| DevOps team members | Highlights release readiness, rollback, monitoring and deployment risks |
| QA-oriented team members | Supports test planning and quality validation |

The product is not meant to replace these roles. It supports their discussion and decision-making.

---

## 6. Proposed Solution

The solution is a Streamlit MVP where the user enters a software task, requirement or idea.

Example input:

`Deploy the new authentication module to production without a rollback plan.`

The app analyses the input and produces two main outputs:

### Risk Analysis

The risk analysis includes:

- Risk Level;
- Risk Score;
- Potential Risks;
- Estimated Impact;
- Mitigation Recommendations;
- Suggested Tests;
- Release Readiness Notes;
- Backlog Improvement Suggestions.

### Generated User Story

The generated backlog output includes:

- User Story;
- Acceptance Criteria;
- Suggested Priority;
- Suggested Story Points;
- Suggested Epic;
- Clarification Questions;
- Definition of Ready checklist.

This makes the output useful both for technical discussion and for Scrum backlog refinement.

---

## 7. MVP Scope

The MVP focuses on the minimum functionality needed to demonstrate the product value.

### In Scope

The MVP includes:

- task or requirement input;
- rule-based risk analysis;
- risk level and risk score generation;
- potential risks and impact explanation;
- mitigation recommendations;
- suggested tests;
- release readiness notes;
- generated user story;
- acceptance criteria in Given / When / Then format;
- suggested priority, story points and epic;
- responsible AI disclaimer.

### Out of Scope

The MVP does not include:

- real Jira API integration;
- user authentication;
- database storage;
- real-time production monitoring;
- enterprise deployment;
- advanced analytics dashboards;
- paid external AI API integration.

These items are considered possible future improvements.

---

## 8. AI Prototype Approach

The MVP does not use a real external AI API.

Instead, it uses deterministic rule-based logic to simulate how an AI-supported assistant could analyse risks and generate backlog-ready user stories.

This approach was chosen because the purpose of the project is to demonstrate Agile, Scrum and DevOps concepts through a functional MVP, while keeping the prototype simple, reproducible and easy to run locally.

In a real production scenario, this logic could be extended with a Large Language Model, but only with appropriate validation, governance and responsible AI controls.

---

## 9. Product Value

AI Risk Detector creates value by helping teams:

- identify risks before implementation;
- improve vague backlog items;
- define clearer acceptance criteria;
- prepare better tests;
- discuss release readiness earlier;
- reduce rework;
- support Sprint Planning and backlog refinement;
- improve collaboration between Agile and DevOps perspectives.

The main value of the product is not automation alone. Its value is in improving the quality of team conversations before work starts.

---

## 10. Project Positioning

AI Risk Detector is positioned as a focused MVP for AI-assisted risk analysis and backlog refinement, demonstrating how Agile, Scrum and DevOps practices can be combined to improve planning, quality and release readiness.

The project connects:

- Agile mindset through iterative MVP delivery;
- Scrum through backlog structure, user stories and Jira;
- DevOps through testing, CI pipeline and release readiness thinking;
- Responsible AI through human validation and clear limitations.

The result is a realistic academic product scenario that demonstrates both a working MVP and the project management concepts behind it.