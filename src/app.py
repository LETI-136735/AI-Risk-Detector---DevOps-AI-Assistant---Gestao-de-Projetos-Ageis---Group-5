"""
AI Risk Detector — DevOps AI Assistant
University Agile Project Management MVP
Run with: pip install streamlit && streamlit run app.py
"""

import streamlit as st
from datetime import datetime

# ──────────────────────────────────────────────
# PAGE CONFIG
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="AI Risk Detector — DevOps AI Assistant",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────
# CUSTOM CSS
# ──────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=IBM+Plex+Sans:wght@300;400;500;600;700&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background-color: #0d1117 !important;
    color: #e6edf3 !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
}
[data-testid="stSidebar"] {
    background-color: #161b22 !important;
    border-right: 1px solid #30363d !important;
}
[data-testid="stSidebar"] * {
    color: #c9d1d9 !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
}
.block-container {
    padding: 2rem 3rem 4rem 3rem !important;
    max-width: 1200px !important;
}

/* Hide the white top bar (Streamlit deploy toolbar) */
[data-testid="stToolbar"],
[data-testid="stDecoration"],
header[data-testid="stHeader"] {
    display: none !important;
    height: 0 !important;
    visibility: hidden !important;
}

.hero-header {
    background: linear-gradient(135deg, #0d1117 0%, #161b22 50%, #1a1f2e 100%);
    border: 1px solid #30363d;
    border-radius: 12px;
    padding: 2rem 2.5rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}
.hero-header::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #58a6ff, #3fb950, #f78166);
}
.hero-title {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 1.8rem !important;
    font-weight: 600 !important;
    color: #58a6ff !important;
    margin: 0 0 0.3rem 0 !important;
    letter-spacing: -0.5px;
}
.hero-subtitle {
    color: #8b949e !important;
    font-size: 0.95rem !important;
    margin: 0 !important;
    font-weight: 300 !important;
}
.hero-meta {
    margin-top: 0.8rem !important;
    font-size: 0.78rem !important;
    color: #6e7681 !important;
    font-family: 'IBM Plex Mono', monospace !important;
}
.card {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 10px;
    padding: 1.5rem;
    margin-bottom: 1.2rem;
}
.card-title {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.78rem;
    font-weight: 600;
    color: #8b949e;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 0.6rem;
}
.card-value {
    font-size: 1.05rem;
    color: #e6edf3;
    line-height: 1.6;
}
.metric-box {
    background: #0d1117;
    border: 1px solid #30363d;
    border-radius: 8px;
    padding: 1rem 1.2rem;
    text-align: center;
}
.metric-label {
    font-size: 0.72rem;
    color: #6e7681;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    font-family: 'IBM Plex Mono', monospace;
    margin-bottom: 0.4rem;
}
.metric-value {
    font-size: 1.8rem;
    font-weight: 700;
    font-family: 'IBM Plex Mono', monospace;
}
.badge-high {
    display: inline-block;
    background: rgba(247, 129, 102, 0.15);
    color: #f78166;
    border: 1px solid rgba(247, 129, 102, 0.4);
    border-radius: 20px;
    padding: 0.25rem 0.9rem;
    font-size: 0.82rem;
    font-weight: 600;
    font-family: 'IBM Plex Mono', monospace;
    letter-spacing: 0.5px;
}
.badge-medium {
    display: inline-block;
    background: rgba(210, 153, 34, 0.15);
    color: #e3b341;
    border: 1px solid rgba(210, 153, 34, 0.4);
    border-radius: 20px;
    padding: 0.25rem 0.9rem;
    font-size: 0.82rem;
    font-weight: 600;
    font-family: 'IBM Plex Mono', monospace;
    letter-spacing: 0.5px;
}
.badge-low {
    display: inline-block;
    background: rgba(63, 185, 80, 0.15);
    color: #3fb950;
    border: 1px solid rgba(63, 185, 80, 0.4);
    border-radius: 20px;
    padding: 0.25rem 0.9rem;
    font-size: 0.82rem;
    font-weight: 600;
    font-family: 'IBM Plex Mono', monospace;
    letter-spacing: 0.5px;
}
.metric-high { color: #f78166; }
.metric-medium { color: #e3b341; }
.metric-low { color: #3fb950; }
.metric-blue { color: #58a6ff; }
.risk-item {
    display: flex;
    align-items: flex-start;
    gap: 0.6rem;
    padding: 0.5rem 0;
    border-bottom: 1px solid #21262d;
    font-size: 0.9rem;
    color: #c9d1d9;
    line-height: 1.5;
}
.risk-item:last-child { border-bottom: none; }
.dot-high { color: #f78166; font-size: 1.1rem; flex-shrink: 0; }
.dot-medium { color: #e3b341; font-size: 1.1rem; flex-shrink: 0; }
.dot-blue { color: #58a6ff; font-size: 1.1rem; flex-shrink: 0; }
.dot-green { color: #3fb950; font-size: 1.1rem; flex-shrink: 0; }
.story-quote {
    background: linear-gradient(90deg, rgba(88,166,255,0.08) 0%, #161b22 100%);
    border-left: 3px solid #58a6ff;
    border-radius: 0 8px 8px 0;
    padding: 1rem 1.2rem;
    font-size: 1rem;
    color: #e6edf3;
    font-style: italic;
    line-height: 1.6;
    margin-bottom: 1rem;
}
.ac-block {
    background: #0d1117;
    border: 1px solid #21262d;
    border-radius: 8px;
    padding: 0.9rem 1.1rem;
    margin-bottom: 0.7rem;
    font-size: 0.87rem;
    color: #c9d1d9;
    line-height: 1.7;
    font-family: 'IBM Plex Mono', monospace;
}
.ac-keyword { color: #58a6ff; font-weight: 600; }
.dor-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.35rem 0;
    font-size: 0.88rem;
    color: #c9d1d9;
}
.check-icon { color: #3fb950; }
.validation-note {
    background: rgba(88,166,255,0.06);
    border: 1px solid rgba(88,166,255,0.25);
    border-radius: 8px;
    padding: 0.9rem 1.2rem;
    font-size: 0.83rem;
    color: #8b949e;
    line-height: 1.6;
    margin-top: 1rem;
}
.stTabs [data-baseweb="tab-list"] {
    background: #161b22 !important;
    border-radius: 8px 8px 0 0 !important;
    border-bottom: 1px solid #30363d !important;
    gap: 0 !important;
    padding: 0 0.5rem !important;
}
.stTabs [data-baseweb="tab"] {
    color: #8b949e !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-size: 0.88rem !important;
    font-weight: 500 !important;
    padding: 0.7rem 1.2rem !important;
    border-radius: 0 !important;
    border-bottom: 2px solid transparent !important;
}
.stTabs [aria-selected="true"] {
    color: #e6edf3 !important;
    border-bottom: 2px solid #58a6ff !important;
    background: transparent !important;
}
.stTabs [data-baseweb="tab-panel"] {
    background: #161b22 !important;
    border: 1px solid #30363d !important;
    border-top: none !important;
    border-radius: 0 0 8px 8px !important;
    padding: 1.5rem !important;
}
.stTextArea textarea {
    background: #161b22 !important;
    border: 1px solid #30363d !important;
    border-radius: 8px !important;
    color: #e6edf3 !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-size: 0.92rem !important;
}
.stTextArea textarea:focus {
    border-color: #58a6ff !important;
    box-shadow: 0 0 0 2px rgba(88,166,255,0.15) !important;
}
.stButton > button {
    background: linear-gradient(135deg, #1f6feb, #1158c7) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.92rem !important;
    padding: 0.6rem 1.6rem !important;
    transition: all 0.2s ease !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #388bfd, #1f6feb) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 16px rgba(31, 111, 235, 0.35) !important;
}
.footer-note {
    text-align: center;
    color: #484f58;
    font-size: 0.76rem;
    font-family: 'IBM Plex Mono', monospace;
    margin-top: 3rem;
    padding-top: 1.5rem;
    border-top: 1px solid #21262d;
}
</style>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────
# KEYWORD DEFINITIONS
# ──────────────────────────────────────────────
HIGH_RISK_KEYWORDS = [
    "production", "deploy", "deployment", "authentication", "login",
    "database", "migration", "payment", "security",
    "rollback missing", "without rollback", "without a rollback",
    "without a rollback plan", "no rollback", "no rollback plan",
    "missing rollback", "urgent", "no testing", "without testing",
]
MEDIUM_RISK_KEYWORDS = [
    "api", "dependency", "integration", "unclear", "requirement",
    "performance", "configuration", "refactor",
]
LOW_RISK_KEYWORDS = [
    "documentation", "text", "copy", "small ui change",
    "internal note", "minor update",
]


# ──────────────────────────────────────────────
# RISK ANALYSIS ENGINE
# ──────────────────────────────────────────────
def analyse_risk(text: str) -> dict:
    t = text.lower()
    high_hits = [kw for kw in HIGH_RISK_KEYWORDS if kw in t]
    medium_hits = [kw for kw in MEDIUM_RISK_KEYWORDS if kw in t]
    low_hits = [kw for kw in LOW_RISK_KEYWORDS if kw in t]

    if len(high_hits) >= 3:
        level = "High"
        score = min(9 + len(high_hits) // 2, 10)
    elif len(high_hits) >= 1:
        score = min(6 + len(high_hits), 9)
        level = "High"
    elif len(medium_hits) >= 1:
        score = min(3 + len(medium_hits), 5)
        level = "Medium"
    else:
        score = max(1, 3 - len(low_hits))
        level = "Low"

    potential_risks = []
    if any(k in t for k in ["authentication", "login"]):
        potential_risks.append("Authentication failure — users may be locked out of the system")
    if any(k in t for k in ["production", "deploy", "deployment"]):
        potential_risks.append("Production outage or failed deployment causing user impact")
    if any(k in t for k in [
        "rollback missing", "without rollback", "without a rollback",
        "without a rollback plan", "no rollback", "no rollback plan",
        "missing rollback"
    ]):
        potential_risks.append("Absence of rollback plan — slow recovery if deployment fails")
    if any(k in t for k in ["database", "migration"]):
        potential_risks.append("Data loss or data inconsistency during migration")
    if "payment" in t:
        potential_risks.append("Transaction failure with direct financial impact")
    if "security" in t:
        potential_risks.append("Security vulnerability or compliance breach")
    if any(k in t for k in ["api", "integration"]):
        potential_risks.append("Integration failure causing downstream dependency issues")
    if any(k in t for k in ["no testing", "without testing"]):
        potential_risks.append("Undetected defects reaching production without test coverage")
    if "monitoring" not in t and level == "High":
        potential_risks.append("Insufficient monitoring — late detection of incidents")
    if not potential_risks:
        potential_risks.append("Low complexity — limited risk exposure identified")

    if level == "High":
        impact = "Critical — potential service disruption, user impact, or data risk. Immediate attention required."
    elif level == "Medium":
        impact = "Moderate — may affect system stability or team velocity if not addressed."
    else:
        impact = "Minimal — change is low-scope and unlikely to affect end users."

    mitigations = []
    if any(k in t for k in ["production", "deploy", "deployment"]):
        mitigations.append("Define and validate a rollback plan before any production release")
        mitigations.append("Use a phased rollout (canary or blue-green deployment) to limit blast radius")
    if any(k in t for k in ["authentication", "login"]):
        mitigations.append("Run authentication regression tests in a staging environment first")
        mitigations.append("Keep the previous authentication module active until the new one is validated")
    if any(k in t for k in ["database", "migration"]):
        mitigations.append("Create a full database backup before executing any migration")
        mitigations.append("Test the migration on a staging environment with production-like data")
    if "payment" in t:
        mitigations.append("Run end-to-end payment flow tests and involve the finance team for sign-off")
    if "security" in t:
        mitigations.append("Conduct a security review and involve the security team before release")
    if any(k in t for k in ["api", "integration"]):
        mitigations.append("Validate API contracts and run integration tests with dependent services")
    if not mitigations:
        mitigations.append("Proceed with standard peer review and testing procedures")
        mitigations.append("Communicate the change to relevant stakeholders before deployment")

    tests = []
    if any(k in t for k in ["authentication", "login"]):
        tests += ["Authentication tests (valid, invalid, expired sessions)", "Security tests for auth flow"]
    if any(k in t for k in ["production", "deploy", "deployment"]):
        tests += ["Regression tests across affected services", "Rollback validation test"]
    if any(k in t for k in ["database", "migration"]):
        tests += ["Database migration tests (forward and rollback)", "Data integrity verification"]
    if "payment" in t:
        tests += ["Payment flow tests (success, failure, edge cases)", "User acceptance testing with finance"]
    if any(k in t for k in ["api", "integration"]):
        tests += ["Integration tests with downstream services", "API contract tests"]
    if not tests:
        tests += ["Smoke tests", "User acceptance testing (UAT)"]
    tests.append("Monitoring verification post-deployment")

    if level == "High":
        readiness = "NOT READY — Several critical risk areas identified. A rollback plan, staging validation, and stakeholder approval are required before proceeding."
    elif level == "Medium":
        readiness = "CONDITIONAL — Address identified gaps (integration tests, dependency review) before scheduling release."
    else:
        readiness = "READY — Risk is low. Standard review and approval process is sufficient."

    backlog = [
        "Add 'Definition of Ready' criteria to this task before sprint commitment",
        "Include acceptance criteria with testable Given/When/Then conditions",
    ]
    if level == "High":
        backlog.append("Consider splitting into smaller, lower-risk tasks if story points are 8+")
        backlog.append("Add a spike to evaluate risk before planning implementation")
    if any(k in t for k in [
        "rollback missing", "without rollback", "without a rollback",
        "without a rollback plan", "no rollback", "no rollback plan",
        "missing rollback"
    ]):
        backlog.append("Create a separate backlog item for rollback plan documentation")

    return {
        "level": level,
        "score": score,
        "high_hits": high_hits,
        "medium_hits": medium_hits,
        "potential_risks": potential_risks,
        "impact": impact,
        "mitigations": mitigations,
        "tests": tests,
        "readiness": readiness,
        "backlog": backlog,
    }


# ──────────────────────────────────────────────
# USER STORY GENERATOR
# ──────────────────────────────────────────────
def infer_role(text: str) -> str:
    t = text.lower()
    if any(k in t for k in ["deploy", "deployment", "release", "rollback", "monitoring", "pipeline", "production"]):
        return "DevOps team member"
    if any(k in t for k in ["backlog", "requirement", "user story", "acceptance criteria", "priority"]):
        return "Product Owner"
    if any(k in t for k in ["sprint", "planning", "review", "retrospective", "blocker"]):
        return "Scrum Master"
    if any(k in t for k in ["test", "bug", "quality", "validation"]):
        return "QA or Developer"
    return "software team member"


def infer_capability_and_benefit(text: str) -> tuple:
    t = text.lower()
    if any(k in t for k in ["deploy", "deployment", "release", "production", "rollback"]):
        return (
            "validate and execute the deployment safely with a defined rollback plan",
            "the team can reduce production risk and ensure service continuity",
        )
    if any(k in t for k in ["authentication", "login"]):
        return (
            "implement and validate the authentication change in a controlled environment",
            "user access is protected and authentication failures are prevented in production",
        )
    if any(k in t for k in ["database", "migration"]):
        return (
            "execute the database migration with a validated rollback and data integrity checks",
            "data loss is prevented and the system remains consistent after the change",
        )
    if "payment" in t:
        return (
            "validate the payment flow end-to-end before any production release",
            "transaction reliability is ensured and financial risk is minimised",
        )
    if any(k in t for k in ["backlog", "requirement", "user story"]):
        return (
            "refine the backlog item with clear acceptance criteria and a Definition of Ready",
            "the development team can plan and implement the feature with confidence",
        )
    if any(k in t for k in ["test", "bug", "quality", "validation"]):
        return (
            "define and execute a comprehensive test plan for this change",
            "defects are caught before release and product quality is maintained",
        )
    if any(k in t for k in ["sprint", "planning", "retrospective"]):
        return (
            "facilitate the Scrum event effectively with a clear agenda and defined outcomes",
            "the team maintains alignment and continuous improvement across sprints",
        )
    return (
        "complete the described task with clear acceptance criteria and adequate testing",
        "the change is delivered reliably without unexpected risk to the system or users",
    )


def infer_epic(text: str) -> str:
    t = text.lower()
    if any(k in t for k in ["deploy", "release", "rollback", "pipeline", "monitoring"]):
        return "DevOps and Release Readiness"
    if any(k in t for k in ["backlog", "requirement", "acceptance criteria"]):
        return "Backlog Quality and Acceptance Criteria"
    if any(k in t for k in ["sprint", "planning", "retrospective", "scrum"]):
        return "Scrum Events Support"
    if any(k in t for k in ["api", "integration", "dependency"]):
        return "Future Integrations"
    if any(k in t for k in ["ai", "responsible", "documentation"]):
        return "Responsible AI and Documentation"
    return "Task Input and Risk Analysis"


def estimate_story_points(risk: dict, text: str) -> int:
    t = text.lower()
    if risk["level"] == "High":
        complex_combo = (
            any(k in t for k in ["production", "deploy"]) and
            any(k in t for k in ["database", "payment", "security", "authentication"]) and
            any(k in t for k in [
                "no rollback", "no rollback plan", "without rollback",
                "without a rollback", "without a rollback plan",
                "rollback missing", "missing rollback", "no testing", "without testing"
            ])
        )
        return 8 if complex_combo else 5
    if risk["level"] == "Medium":
        return 3
    return 2 if len(risk["high_hits"]) == 0 and len(risk["medium_hits"]) == 0 else 1


def infer_priority(risk: dict) -> tuple:
    if risk["level"] == "High":
        return 4, "Must Have / Critical"
    if risk["level"] == "Medium":
        return 3, "High"
    return 2, "Medium"


def build_acceptance_criteria(text: str, risk: dict) -> list:
    t = text.lower()
    criteria = []
    if any(k in t for k in [
        "rollback missing", "without rollback", "without a rollback",
        "without a rollback plan", "no rollback", "no rollback plan",
        "missing rollback"
    ]): 
        criteria.append(
            "**Given** the task is ready to be deployed,\n"
            "**When** the release is being prepared,\n"
            "**Then** a rollback plan must be defined, documented, and validated."
        )
    if any(k in t for k in ["authentication", "login"]):
        criteria.append(
            "**Given** the authentication module is deployed,\n"
            "**When** users attempt to log in,\n"
            "**Then** authentication must succeed for valid users and fail securely for invalid credentials."
        )
    if any(k in t for k in ["production", "deploy", "deployment"]):
        criteria.append(
            "**Given** the deployment is executed in production,\n"
            "**When** monitoring tools are active,\n"
            "**Then** errors and performance degradation must be detected and alerted within 5 minutes."
        )
    if any(k in t for k in ["database", "migration"]):
        criteria.append(
            "**Given** the database migration is about to run,\n"
            "**When** the migration executes,\n"
            "**Then** all data must remain consistent and the rollback script must be tested and available."
        )
    if "payment" in t:
        criteria.append(
            "**Given** the payment flow is updated,\n"
            "**When** a transaction is initiated,\n"
            "**Then** the payment must complete successfully or fail with a user-friendly error and no financial loss."
        )
    if any(k in t for k in ["api", "integration"]):
        criteria.append(
            "**Given** the integration with the external service is configured,\n"
            "**When** the system makes an API call,\n"
            "**Then** the response must be handled correctly including error and timeout scenarios."
        )
    if len(criteria) < 3:
        criteria.append(
            "**Given** the task has been completed and reviewed,\n"
            "**When** the change is submitted for release,\n"
            "**Then** all acceptance criteria must be met and verified by a peer reviewer."
        )
    if len(criteria) < 3:
        criteria.append(
            "**Given** the change is deployed,\n"
            "**When** post-deployment checks are run,\n"
            "**Then** the system must perform within expected parameters and no critical errors are logged."
        )
    if len(criteria) < 3:
        criteria.append(
            "**Given** the task is considered complete,\n"
            "**When** the Product Owner reviews the output,\n"
            "**Then** the deliverable must match the agreed scope and meet the Definition of Done."
        )
    return criteria[:4]


def build_clarification_questions(text: str, risk: dict) -> list:
    t = text.lower()
    questions = []
    if any(k in t for k in ["production", "deploy"]):
        questions.append("Has a rollback plan been defined and tested for this deployment?")
        questions.append("What is the deployment window and who is on-call for incident response?")
    if any(k in t for k in ["authentication", "login"]):
        questions.append("Has the authentication change been tested in a staging environment?")
    if any(k in t for k in ["database", "migration"]):
        questions.append("Is there a full database backup available before the migration runs?")
    if "payment" in t:
        questions.append("Has finance or a payment specialist reviewed and signed off on this change?")
    if risk["level"] == "High" and not any(k in t for k in ["test", "testing"]):
        questions.append("What is the test plan for this change? Who is responsible for QA sign-off?")
    if not questions:
        questions.append("What is the expected completion timeline and who owns this task?")
        questions.append("Are there any dependencies or blocked tasks that need to be resolved first?")
    return questions


def generate_user_story(text: str, risk: dict) -> dict:
    role = infer_role(text)
    capability, benefit = infer_capability_and_benefit(text)
    epic = infer_epic(text)
    story_points = estimate_story_points(risk, text)
    priority_score, priority_label = infer_priority(risk)
    criteria = build_acceptance_criteria(text, risk)
    questions = build_clarification_questions(text, risk)
    dor = [
        "User story is written in 'As a / I want / So that' format",
        "Acceptance criteria are defined in Given/When/Then format",
        "Story has been reviewed by the Product Owner",
        "Dependencies and blockers are identified",
        "Story has been estimated by the development team",
        "Non-functional requirements (performance, security) are noted",
        "Definition of Done is agreed upon by the team",
    ]
    story_text = f"As a {role}, I want to {capability}, so that {benefit}."
    return {
        "story": story_text,
        "criteria": criteria,
        "priority_score": priority_score,
        "priority_label": priority_label,
        "story_points": story_points,
        "epic": epic,
        "questions": questions,
        "dor": dor,
    }


# ──────────────────────────────────────────────
# SIDEBAR
# ──────────────────────────────────────────────
def render_sidebar():
    with st.sidebar:
        st.markdown("### 🛡️ AI Risk Detector")
        st.markdown("**DevOps AI Assistant — MVP**")
        st.markdown("---")
        st.markdown("**📌 Project Context**")
        st.markdown(
            "University Agile Project Management course. "
            "This MVP demonstrates Sprint 2 delivery using Scrum, DevOps thinking, "
            "and responsible AI use."
        )
        st.markdown("---")
        st.markdown("**⚙️ What this app does**")
        st.markdown(
            "- Analyses risk in software tasks using rule-based logic  \n"
            "- Generates a structured user story for the Product Backlog  \n"
            "- Produces a Jira-ready summary for immediate use  \n"
        )
        st.markdown("---")
        st.markdown("**🔄 Scrum Relevance**")
        st.markdown(
            "Supports Sprint Planning, Backlog Refinement, and the Definition of Ready. "
            "Helps the Scrum Master and Product Owner surface risk early."
        )
        st.markdown("---")
        st.markdown("**🚀 DevOps Relevance**")
        st.markdown(
            "Encourages shift-left risk detection, release readiness checks, "
            "and rollback awareness — core DevOps practices."
        )
        st.markdown("---")
        st.markdown("**🤖 Responsible AI**")
        st.markdown(
            "This MVP uses **deterministic rule-based logic** instead of a live AI API. "
            "This means:  \n"
            "- No API keys or external costs  \n"
            "- Fully reproducible and auditable outputs  \n"
            "- Easy to run offline and in academic settings  \n\n"
            "In a production context, this logic could be replaced with a real LLM "
            "after appropriate evaluation and governance."
        )
        st.markdown("---")
        st.markdown(
            "<small style='color:#484f58;'>AI Risk Detector v1.0 · Sprint 2 · MVP</small>",
            unsafe_allow_html=True,
        )


# ──────────────────────────────────────────────
# RENDER HELPERS
# ──────────────────────────────────────────────
def render_risk_badge(level: str) -> str:
    css = {"High": "badge-high", "Medium": "badge-medium", "Low": "badge-low"}
    return f'<span class="{css.get(level, "badge-low")}">{level} Risk</span>'


def render_score_color(level: str) -> str:
    return {"High": "metric-high", "Medium": "metric-medium", "Low": "metric-low"}.get(level, "metric-low")


def render_risk_tab(risk: dict):
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f'<div class="metric-box"><div class="metric-label">Risk Level</div>{render_risk_badge(risk["level"])}</div>', unsafe_allow_html=True)
    with c2:
        color_cls = render_score_color(risk["level"])
        st.markdown(f'<div class="metric-box"><div class="metric-label">Risk Score</div><div class="metric-value {color_cls}">{risk["score"]}<span style="font-size:1rem;color:#6e7681">/10</span></div></div>', unsafe_allow_html=True)
    with c3:
        kw_count = len(risk["high_hits"]) + len(risk["medium_hits"])
        st.markdown(f'<div class="metric-box"><div class="metric-label">Keywords Matched</div><div class="metric-value metric-blue">{kw_count}</div></div>', unsafe_allow_html=True)
    with c4:
        ready_color = "metric-high" if "NOT" in risk["readiness"] else ("metric-medium" if "CONDITIONAL" in risk["readiness"] else "metric-low")
        ready_label = "Not Ready" if "NOT" in risk["readiness"] else ("Conditional" if "CONDITIONAL" in risk["readiness"] else "Ready")
        st.markdown(f'<div class="metric-box"><div class="metric-label">Release Readiness</div><div class="metric-value {ready_color}" style="font-size:1.1rem;padding-top:0.3rem">{ready_label}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    left, right = st.columns(2)

    with left:
        st.markdown('<div class="card"><div class="card-title">⚠️ Potential Risks</div>', unsafe_allow_html=True)
        for r in risk["potential_risks"]:
            st.markdown(f'<div class="risk-item"><span class="dot-high">▸</span><span>{r}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown(f'<div class="card"><div class="card-title">💥 Estimated Impact</div><div class="card-value">{risk["impact"]}</div></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card"><div class="card-title">🚦 Release Readiness</div><div class="card-value">{risk["readiness"]}</div></div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="card"><div class="card-title">🛡️ Mitigation Recommendations</div>', unsafe_allow_html=True)
        for m in risk["mitigations"]:
            st.markdown(f'<div class="risk-item"><span class="dot-green">▸</span><span>{m}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card"><div class="card-title">🧪 Suggested Tests</div>', unsafe_allow_html=True)
        for t in risk["tests"]:
            st.markdown(f'<div class="risk-item"><span class="dot-blue">▸</span><span>{t}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card"><div class="card-title">📋 Backlog Improvement Suggestions</div>', unsafe_allow_html=True)
        for b in risk["backlog"]:
            st.markdown(f'<div class="risk-item"><span class="dot-medium">▸</span><span>{b}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="validation-note">🤖 <strong>Human Validation Note:</strong> AI-generated recommendations must be reviewed by the Product Owner, Scrum Master, Developers or relevant stakeholders before being used for planning, development or release decisions.</div>', unsafe_allow_html=True)


def render_story_tab(story: dict, risk: dict):
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f'<div class="metric-box"><div class="metric-label">Priority Score</div><div class="metric-value metric-blue">{story["priority_score"]}</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="metric-box"><div class="metric-label">Story Points</div><div class="metric-value metric-blue">{story["story_points"]} SP</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown(f'<div class="metric-box"><div class="metric-label">Priority Label</div><div class="metric-value" style="font-size:0.95rem;padding-top:0.5rem;color:#e3b341">{story["priority_label"]}</div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown(f'<div class="metric-box"><div class="metric-label">Suggested Epic</div><div class="metric-value" style="font-size:0.78rem;padding-top:0.5rem;color:#8b949e;line-height:1.3">{story["epic"]}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f'<div class="card"><div class="card-title">📖 User Story</div><div class="story-quote">{story["story"]}</div></div>', unsafe_allow_html=True)

    left, right = st.columns(2)
    with left:
        st.markdown('<div class="card"><div class="card-title">✅ Acceptance Criteria (Given / When / Then)</div>', unsafe_allow_html=True)
        for i, c in enumerate(story["criteria"], 1):
            formatted = c.replace("**Given**", '<span class="ac-keyword">Given</span>') \
                         .replace("**When**", '<span class="ac-keyword">When</span>') \
                         .replace("**Then**", '<span class="ac-keyword">Then</span>')
            st.markdown(f'<div class="ac-block"><strong>AC{i}</strong><br>{formatted}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="card"><div class="card-title">❓ Clarification Questions</div>', unsafe_allow_html=True)
        for q in story["questions"]:
            st.markdown(f'<div class="risk-item"><span class="dot-medium">?</span><span>{q}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="card"><div class="card-title">📌 Definition of Ready Checklist</div>', unsafe_allow_html=True)
        for d in story["dor"]:
            st.markdown(f'<div class="dor-item"><span class="check-icon">✓</span><span>{d}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="validation-note">🤖 <strong>Human Validation Note:</strong> AI-generated recommendations must be reviewed by the Product Owner, Scrum Master, Developers or relevant stakeholders before being used for planning, development or release decisions.</div>', unsafe_allow_html=True)


# ──────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────
SAMPLE_INPUT = "Deploy the new authentication module to production without a rollback plan."

def main():
    render_sidebar()

    st.markdown("""
    <div class="hero-header">
        <div class="hero-title">🛡️ AI Risk Detector</div>
        <div class="hero-subtitle">DevOps AI Assistant — Agile Project Management MVP · Sprint 2</div>
        <div class="hero-meta">Rule-based risk analysis &nbsp;·&nbsp; User story generation</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### 📝 Task Input")
    col_input, col_btn = st.columns([5, 1])
    with col_btn:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Load example", key="sample"):
            st.session_state["task_input"] = SAMPLE_INPUT
    with col_input:
        user_input = st.text_area(
            "task",
            value=st.session_state.get("task_input", ""),
            height=110,
            placeholder='e.g. "Deploy the new authentication module to production without a rollback plan."',
            key="task_input",
            label_visibility="collapsed",
        )

    analyse = st.button("🔍 Analyse Risk and Generate User Story", key="analyse")

    if analyse:
        if not user_input or not user_input.strip():
            st.warning("Please enter a task description before analysing.")
            return

        risk = analyse_risk(user_input)
        story = generate_user_story(user_input, risk)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown("### 📊 Analysis Results")

        tab1, tab2 = st.tabs(["🔴 Risk Analysis", "📖 Generated User Story"])
        with tab1:
            render_risk_tab(risk)
        with tab2:
            render_story_tab(story, risk)

    st.markdown("""
    <div class="footer-note">
        AI Risk Detector · DevOps AI Assistant · Agile Project Management MVP · Sprint 2<br><br>
        pip install streamlit &nbsp;·&nbsp; streamlit run app.py
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()