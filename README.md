# AI Risk Detector ⚠️
## Project Overview
**AI Risk Detector** is an MVP developed to support software teams in planning and quality assurance activities. The tool leverages **Artificial Intelligence** to analyze technical tasks and generate risk reports, addressing common issues such as ambiguous requirements and lack of visibility in the workflow.

This project is developed as part of the **Agile Project Management** (2026) course, integrating Scrum and DevOps methodologies to solve real-world software delivery challenges.

## Our Process
To deliver this increment, the team followed a structured Agile approach:
1. **Problem Definition:** We identified key risks in software tasks and proposed an AI-driven solution.
2. **Product Backlog:** We defined and prioritized User Stories to guide development.
3. **Sprint Planning:** Work was organized into Sprint 1 using a dedicated Scrum board.
4. **Development:** We built a functional application that implements core risk analysis using AI.

## Features (Sprint 1)
* **Task Input Interface:** A text area for users to describe software tasks in natural language.
* **AI-Powered Risk Analysis:** Integration with language models to process inputs and return structured assessments.
* **Analysis Output:** A clear display of the risk level (High, Medium, Low), a list of potential risks, estimated impact, and actionable mitigation recommendations.

## Methodology
* **Scrum:** Iterative management through sprints, maintaining transparency with a prioritized Product Backlog.
* **DevOps:** Continuous delivery mindset using a centralized repository and structured environments.

## Installation and Local Usage

### Prerequisites
* Python 3.9 or higher.
* An OpenAI API Key (Optional: the application includes a "mock mode" if no key is detected).

### Steps to Run
1. **Clone the repository:**
   ```bash
   git clone [YOUR-REPOSITORY-URL]
   cd [YOUR-FOLDER-NAME]
   ```
2. **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the application with Streamlit:**
    ```bash
    streamlit run app.py
    ```

## Repository Structure
* `/src`: Application source code.
* `/docs`: Technical documentation and Sprint 1 reflections.
* `/management`: Scrum management evidence, including the Product Backlog and Sprint 1 board.
* `requirements.txt`: System dependencies file.