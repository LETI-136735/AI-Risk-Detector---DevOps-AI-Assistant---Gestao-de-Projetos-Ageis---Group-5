import streamlit as st
import os
import re

# Intentamos importar OpenAI; si no está disponible, usamos mock
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

# --- Configuración de la página ---
st.set_page_config(
    page_title="AI Risk Detector",
    page_icon="⚠️",
    layout="centered",
)

# --- Prompt del sistema que fuerza el formato de respuesta ---
SYSTEM_PROMPT = """You are a software risk analysis expert for Agile development teams.
When given a software task, you must respond EXACTLY in this format (no deviations):

Risks:
- [risk 1]
- [risk 2]
- [risk 3]

Risk Level:
[High / Medium / Low]

Impact:
[One paragraph describing the overall impact]

Recommendations:
- [recommendation 1]
- [recommendation 2]
- [recommendation 3]

Do not include any other text, headers, or formatting outside of this structure."""


def get_mock_response(task: str) -> str:
    """Respuesta de ejemplo cuando no hay API key disponible."""
    return f"""Risks:
- Potential downtime during the execution of "{task}"
- Incomplete rollback plan if something fails
- Dependencies not properly validated before starting

Risk Level:
High

Impact:
Executing "{task}" without proper preparation could lead to service interruptions, data inconsistencies, or cascading failures in dependent systems. The team's velocity may be significantly impacted if recovery takes longer than expected.

Recommendations:
- Create a detailed rollback plan before proceeding
- Run the task in a staging environment first to identify issues early
- Notify all stakeholders and schedule a maintenance window to minimise user impact"""


def call_ai_api(task: str) -> str:
    """Llama a la API de OpenAI y devuelve la respuesta en texto plano."""
    api_key = os.environ.get("OPENAI_API_KEY", "")

    # Si no hay clave o OpenAI no está instalado, devolvemos el mock
    if not api_key or not OPENAI_AVAILABLE:
        return get_mock_response(task)

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Analyse the following software task: {task}"},
        ],
        temperature=0.4,
        max_tokens=600,
    )

    return response.choices[0].message.content.strip()


def parse_response(raw: str) -> dict:
    """Extrae las secciones del texto de respuesta del modelo."""
    sections = {
        "risks": [],
        "risk_level": "",
        "impact": "",
        "recommendations": [],
    }

    # Separamos el texto en bloques por sección
    risks_match = re.search(r"Risks:\s*([\s\S]*?)(?=Risk Level:)", raw)
    level_match = re.search(r"Risk Level:\s*(.+)", raw)
    impact_match = re.search(r"Impact:\s*([\s\S]*?)(?=Recommendations:)", raw)
    recs_match = re.search(r"Recommendations:\s*([\s\S]*?)$", raw)

    if risks_match:
        lines = risks_match.group(1).strip().splitlines()
        sections["risks"] = [l.lstrip("- ").strip() for l in lines if l.strip()]

    if level_match:
        sections["risk_level"] = level_match.group(1).strip()

    if impact_match:
        sections["impact"] = impact_match.group(1).strip()

    if recs_match:
        lines = recs_match.group(1).strip().splitlines()
        sections["recommendations"] = [l.lstrip("- ").strip() for l in lines if l.strip()]

    return sections


def display_results(sections: dict):
    """Muestra los resultados estructurados en la interfaz."""

    # Color del badge según el nivel de riesgo
    level = sections["risk_level"].lower()
    if "high" in level:
        badge_color = "#d32f2f"
    elif "medium" in level:
        badge_color = "#f57c00"
    else:
        badge_color = "#388e3c"

    # --- Nivel de riesgo ---
    st.markdown("### Risk Level")
    st.markdown(
        f"<span style='background-color:{badge_color}; color:white; padding:6px 16px; "
        f"border-radius:6px; font-weight:bold; font-size:1.1em;'>"
        f"{sections['risk_level']}</span>",
        unsafe_allow_html=True,
    )
    st.markdown("")

    # --- Riesgos identificados ---
    st.markdown("### Risks")
    if sections["risks"]:
        for risk in sections["risks"]:
            st.markdown(f"- {risk}")
    else:
        st.info("No specific risks identified.")

    # --- Impacto ---
    st.markdown("### Impact")
    st.write(sections["impact"] if sections["impact"] else "No impact description available.")

    # --- Recomendaciones ---
    st.markdown("### Recommendations")
    if sections["recommendations"]:
        for rec in sections["recommendations"]:
            st.markdown(f"- {rec}")
    else:
        st.info("No recommendations available.")


# ============================================================
# INTERFAZ PRINCIPAL
# ============================================================

st.title("⚠️ AI Risk Detector")
st.caption("Analyse your software tasks and identify risks before they materialise.")
st.divider()

# Campo de texto para la tarea
task_input = st.text_area(
    label="Describe your software task",
    placeholder="e.g. deploy to production, merge feature branch, update database schema...",
    height=120,
)

# Botón de análisis (desactivado si el input está vacío)
analyze_button = st.button(
    "Analyze Risk",
    type="primary",
    disabled=(not task_input.strip()),
)

# --- Lógica principal al pulsar el botón ---
if analyze_button and task_input.strip():
    with st.spinner("Analysing risks... please wait."):
        try:
            raw_response = call_ai_api(task_input.strip())
            sections = parse_response(raw_response)

            st.divider()
            st.markdown("## Analysis Results")
            display_results(sections)

            # Opción para iniciar un nuevo análisis
            st.divider()
            if st.button("🔄 New Analysis"):
                st.rerun()

        except Exception as e:
            st.error(
                "Something went wrong while processing your request. "
                "Please try again in a moment."
            )
            # Log interno sin exponer detalles técnicos al usuario
            st.session_state["last_error"] = str(e)

# --- Aviso si no hay API key ---
if not os.environ.get("OPENAI_API_KEY") or not OPENAI_AVAILABLE:
    st.sidebar.warning(
        "⚠️ **Mock mode active**\n\n"
        "No OpenAI API key detected. The app is using a pre-built example response.\n\n"
        "To use the real AI model, set the `OPENAI_API_KEY` environment variable and "
        "install the `openai` package (`pip install openai`)."
    )
