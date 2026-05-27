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

```text
Deploy the new authentication module to production without a rollback plan.
