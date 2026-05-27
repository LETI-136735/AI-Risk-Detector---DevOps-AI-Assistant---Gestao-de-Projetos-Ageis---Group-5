import pytest

from src.app import (
    analyse_risk,
    generate_user_story,
    infer_role,
    infer_epic,
)


def test_high_risk_deployment_without_rollback():
    text = "Deploy the new authentication module to production without rollback."

    result = analyse_risk(text)

    assert result["level"] == "High"
    assert result["score"] >= 8
    assert any("rollback" in risk.lower() for risk in result["potential_risks"])
    assert any("authentication" in risk.lower() for risk in result["potential_risks"])
    assert any("Rollback" in test or "rollback" in test for test in result["tests"])


def test_low_risk_documentation_change():
    text = "Update internal documentation copy for the onboarding page."

    result = analyse_risk(text)

    assert result["level"] == "Low"
    assert result["score"] <= 3
    assert result["impact"].startswith("Minimal")


def test_medium_risk_api_integration_change():
    text = "Refactor the API integration dependency configuration."

    result = analyse_risk(text)

    assert result["level"] == "Medium"
    assert result["score"] >= 3
    assert any("Integration" in test or "API" in test for test in result["tests"])


def test_user_story_generation_for_deployment_task():
    text = "Deploy the new authentication module to production without a rollback plan."

    risk = analyse_risk(text)
    story = generate_user_story(text, risk)

    assert story["story"].startswith("As a DevOps team member")
    assert "rollback" in story["story"].lower() or "deployment" in story["story"].lower()
    assert story["priority_score"] == 4
    assert story["story_points"] in [5, 8]
    assert story["epic"] == "DevOps and Release Readiness"


def test_generated_acceptance_criteria_have_given_when_then():
    text = "Deploy the new authentication module to production without a rollback plan."

    risk = analyse_risk(text)
    story = generate_user_story(text, risk)

    assert len(story["criteria"]) >= 3

    all_criteria_text = " ".join(story["criteria"]).lower()

    assert "given" in all_criteria_text
    assert "when" in all_criteria_text
    assert "then" in all_criteria_text


def test_role_inference_for_scrum_context():
    text = "Improve Sprint Planning to identify blockers before the sprint starts."

    role = infer_role(text)

    assert role == "Scrum Master"


def test_epic_inference_for_backlog_context():
    text = "Improve backlog requirements and acceptance criteria."

    epic = infer_epic(text)

    assert epic == "Backlog Quality and Acceptance Criteria"


def test_empty_or_generic_task_still_returns_valid_structure():
    text = "Small internal update."

    risk = analyse_risk(text)
    story = generate_user_story(text, risk)

    assert "level" in risk
    assert "score" in risk
    assert "potential_risks" in risk
    assert "story" in story
    assert "criteria" in story
    assert "priority_score" in story
    assert "story_points" in story