import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app")))

from app import calculate_score


def test_required_skill_score():
    caregiver = {
        "skills": ["Dementia", "Personal Care"],
        "availability": "Mon-Fri",
        "location": "Philadelphia",
        "compliance": True
    }

    score, reasons = calculate_score(
        caregiver,
        "Dementia",
        "Philadelphia"
    )

    assert score == 100
    assert "Required skill" in reasons


def test_location_match():
    caregiver = {
        "skills": [],
        "availability": "Mon-Fri",
        "location": "Philadelphia",
        "compliance": False
    }

    score, reasons = calculate_score(
        caregiver,
        "Dementia",
        "Philadelphia"
    )

    assert score == 40
    assert "Location match" in reasons


def test_compliance_score():
    caregiver = {
        "skills": [],
        "availability": "Tue-Sun",
        "location": "Upper Darby",
        "compliance": True
    }

    score, reasons = calculate_score(
        caregiver,
        "Dementia",
        "Philadelphia"
    )

    assert score == 20
    assert "Compliant" in reasons


def test_no_matching_factors():
    caregiver = {
        "skills": ["Companion Care"],
        "availability": "Tue-Sun",
        "location": "Upper Darby",
        "compliance": False
    }

    score, reasons = calculate_score(
        caregiver,
        "Dementia",
        "Philadelphia"
    )

    assert score == 0
    assert reasons == []