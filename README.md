# AI Risk Detector — DevOps AI Assistant

<p align="center">
  <strong>Agile Project Management · Group 5</strong><br>
  AI-supported MVP for risk analysis, backlog improvement and user story generation.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue" />
  <img src="https://img.shields.io/badge/Streamlit-MVP-red" />
  <img src="https://img.shields.io/badge/Tests-Pytest-green" />
  <img src="https://img.shields.io/badge/CI-GitHub%20Actions-black" />
  <img src="https://img.shields.io/badge/Scrum-Jira-blueviolet" />
</p>

---

## Overview

**AI Risk Detector** is a lightweight MVP designed to support Agile and DevOps software teams before implementation or release.

The app receives a software task, requirement or idea and produces:

| Output | Purpose |
|---|---|
| Risk Analysis | Identify delivery, technical and release risks early |
| User Story | Convert vague requirements into backlog-ready stories |
| Acceptance Criteria | Support clearer Definition of Ready and Done |
| Suggested Tests | Improve quality and release confidence |
| Release Readiness Notes | Help teams prepare safer deployments |

The project is not intended to be a production-ready AI platform. It is an academic MVP used to demonstrate **Agile Project Management, Scrum, DevOps and responsible AI thinking**.

---

## MVP Demo Flow

```text
Input:
Deploy the new authentication module to production without a rollback plan.

Output:
Risk Level: High
Potential Risks: authentication failure, production outage, missing rollback
Suggested Tests: authentication tests, regression tests, rollback validation
Generated User Story: As a DevOps team member...
Acceptance Criteria: Given / When / Then
