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

AI Risk Detector is positioned as a focused MVP for AI-assisted risk analysis and backlog refinement, demonstrating how Agile, Scrum and DevOps practices can be combined to improve planning, quality and release readiness.

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
