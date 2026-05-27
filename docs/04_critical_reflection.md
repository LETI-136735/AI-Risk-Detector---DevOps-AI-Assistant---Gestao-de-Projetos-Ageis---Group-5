# Critical Reflection

## 1. Introduction

This document provides a critical reflection on the use of **Artificial Intelligence, Scrum and DevOps** in the AI Risk Detector project.

The project demonstrates a lightweight MVP that supports Agile and DevOps teams by analysing software tasks, identifying risks and generating backlog-ready user stories.

The purpose of this reflection is not only to describe what was built, but to evaluate what was learned, what worked well, what limitations exist and how AI can responsibly support software teams.

---

## 2. AI in Agile Teams

Artificial Intelligence can support Agile teams by improving the quality of information available before work starts.

In this project, AI Risk Detector was designed to support activities such as:

- identifying risks in software tasks;
- improving vague requirements;
- generating user stories;
- suggesting acceptance criteria;
- recommending tests;
- supporting release readiness discussion.

This can help Agile teams because many problems in software delivery start before implementation. If a backlog item is unclear, too large, risky or missing acceptance criteria, the sprint may be affected later.

AI can help by making hidden risks more visible earlier.

However, AI should not be treated as a replacement for team discussion. Agile values collaboration, feedback and shared understanding. If a team accepts AI-generated output without discussion, it may reduce critical thinking instead of improving it.

For this reason, in this project AI is treated as a **decision-support tool**, not as an automatic decision-maker.

---

## 3. AI and Scrum

Scrum depends heavily on transparency, inspection and adaptation.

AI Risk Detector can support Scrum by improving the quality of Scrum artifacts and events.

### Product Backlog

The app supports the Product Backlog by transforming vague tasks into more structured user stories.

For example, a vague deployment task can be converted into:

- a user story;
- acceptance criteria;
- suggested priority;
- story points;
- suggested epic;
- clarification questions.

This can help the team refine the backlog before Sprint Planning.

### Sprint Planning

During Sprint Planning, the team needs to understand the work selected for the sprint.

AI Risk Detector can support Sprint Planning by identifying risks, missing tests, unclear acceptance criteria or release concerns before the team commits to work.

This improves the quality of planning because the team can discuss risk before the sprint starts.

### Sprint Review

During Sprint Review, the team inspects what was delivered.

The initial AI risk analysis can be compared with the actual increment. This helps the team discuss whether the identified risks were addressed and whether the work is ready for release.

### Sprint Retrospective

In Retrospective, the team reflects on how to improve.

AI Risk Detector could help identify recurring patterns, such as repeated missing rollback plans, unclear user stories or insufficient test planning.

This makes AI useful not only for individual tasks, but also for continuous improvement.

---

## 4. AI and DevOps

DevOps focuses on improving the connection between development, testing, delivery and operation.

AI Risk Detector connects with DevOps because it helps teams think about delivery risks earlier.

The app can identify risks related to:

- production deployment;
- missing rollback plans;
- insufficient testing;
- monitoring gaps;
- database migration;
- authentication;
- API integration;
- security or payment-related changes.

This supports a shift-left approach, where risks are identified earlier instead of being discovered during deployment or production operation.

The MVP also supports DevOps thinking by suggesting:

- regression tests;
- integration tests;
- rollback validation;
- monitoring verification;
- release readiness actions.

In addition, the project itself includes basic DevOps evidence:

- GitHub repository;
- version control;
- automated tests with pytest;
- GitHub Actions CI pipeline.

This means DevOps was applied both in the product concept and in the delivery of the project.

---

## 5. Human-in-the-Loop Principle

A central principle of this project is that AI should support humans, not replace them.

The app includes a human validation note:

> AI-generated recommendations must be reviewed by the Product Owner, Scrum Master, Developers or relevant stakeholders before being used for planning, development or release decisions.

This is important because AI-generated output may be incomplete, inaccurate or not fully adapted to the real project context.

In Agile and DevOps environments, accountability remains with the team.

AI can suggest risks, tests or acceptance criteria, but humans must decide:

- whether the risk is relevant;
- whether the acceptance criteria are correct;
- whether the suggested tests are sufficient;
- whether the item is ready for a sprint;
- whether a release should proceed.

This human-in-the-loop approach reduces the risk of overconfidence in automated recommendations.

---

## 6. Risks of AI Use

Although AI can create value, it also introduces risks.

### Hallucination

A real AI model can generate information that sounds correct but is not accurate.

In software projects, this could lead to wrong assumptions, incorrect technical recommendations or incomplete acceptance criteria.

### Bias

AI systems can reflect bias from training data or design assumptions.

This may affect how recommendations are generated or which risks are prioritised.

### Overconfidence

Teams may trust AI output too much because it appears structured and professional.

This is dangerous because a well-written recommendation is not necessarily correct.

### Lack of Context

AI may not understand the full organisational, technical or business context.

For example, it may not know:

- system architecture;
- team capacity;
- production constraints;
- legal requirements;
- business priorities;
- stakeholder expectations.

### Privacy and Data Sensitivity

If a real AI API were used, entering sensitive project information could create privacy or security concerns.

This is especially relevant when dealing with production systems, customers, financial flows or security issues.

---

## 7. Why the MVP Uses Rule-Based Logic

The MVP does not use a real external AI API.

Instead, it uses deterministic rule-based logic to simulate AI-supported risk analysis and user story generation.

This decision has several advantages:

| Advantage | Explanation |
|---|---|
| Simplicity | The app can run locally without external services |
| Reproducibility | The same input produces the same output |
| No cost | No paid API is required |
| Privacy | No task data is sent to external systems |
| Stability | The demo does not depend on internet access or API availability |
| Academic focus | The project can focus on Agile, Scrum and DevOps concepts |

This limitation is also important to recognise.

The rule-based MVP is not as flexible or intelligent as a real AI model. It cannot fully understand complex language, hidden context or unusual scenarios.

However, it is sufficient to demonstrate the product idea and support the academic objectives of the assignment.

---

## 8. Project Limitations

The project has several limitations.

| Limitation | Explanation |
|---|---|
| Rule-based AI | The app simulates AI behaviour but does not use a real model |
| Limited context | The app only analyses the text entered by the user |
| No Jira API integration | User stories must be copied manually into Jira |
| No database | Inputs and outputs are not stored |
| No real monitoring | The app suggests monitoring but does not connect to operational systems |
| Limited UI testing | Automated tests focus on logic, not the visual interface |
| Basic CI pipeline | The pipeline runs tests but does not include full deployment automation |
| Academic scope | The product is an MVP, not a production-ready enterprise tool |

These limitations do not invalidate the project. Instead, they define the boundary of the MVP and help identify future improvements.

---

## 9. Lessons Learned

Several lessons were learned during the project.

### Agile Lesson

A lightweight MVP is more useful than an overcomplicated unfinished product.

The team focused on the core value: analysing risk and generating user stories. This made the project easier to demonstrate and align with the assignment.

### Scrum Lesson

Scrum helps structure uncertainty.

By using epics, user stories, acceptance criteria, story points and sprint allocation, the team transformed a broad idea into manageable work items.

Jira helped make this work visible.

### DevOps Lesson

DevOps is not only about tools.

Although the project includes tests and a CI pipeline, the most important DevOps lesson is the focus on quality, feedback and release readiness.

The MVP itself supports DevOps thinking by highlighting testing, rollback and monitoring concerns.

### AI Lesson

AI creates value when it improves clarity, but it creates risk when teams stop thinking critically.

The project shows that AI should support discussion, not replace judgement.

---

## 10. Future Improvements

Future improvements could include:

- real AI model integration;
- Jira API integration;
- export of generated user stories directly to Jira;
- storage of previous analyses;
- dashboard for recurring risks;
- stronger test coverage;
- deployment to a cloud environment;
- monitoring and logging;
- security and privacy controls;
- better AI governance and auditability.

These improvements would make the product more mature, but they were outside the current MVP scope.

---

## 11. Conclusion

AI Risk Detector demonstrates how Agile, Scrum, DevOps and AI can be connected in a practical project scenario.

Agile was reflected through the MVP approach and iterative improvement.

Scrum was reflected through the Product Backlog, user stories, acceptance criteria, sprint allocation and Jira board.

DevOps was reflected through version control, automated tests, CI pipeline and release readiness thinking.

AI was used as a support mechanism to improve risk visibility and backlog quality.

The key conclusion is that AI can support Agile and DevOps teams, but it must be used responsibly. It should improve human decision-making, not replace it.

The project therefore shows that the value of AI in software teams is not only automation. Its value is helping teams ask better questions, identify risks earlier and make better decisions before implementation or release.