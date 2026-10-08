from flask import Flask, render_template

app = Flask(__name__)


def calculate_score(caregiver, required_skill, required_location):
    score = 0
    reasons = []

    if required_skill in caregiver["skills"]:
        score += 40
        reasons.append("Required skill")

    if caregiver["availability"] == "Mon-Fri":
        score += 20
        reasons.append("Available")

    if caregiver["location"] == required_location:
        score += 20
        reasons.append("Location match")

    if caregiver["compliance"]:
        score += 20
        reasons.append("Compliant")

    return score, reasons


@app.route("/")
def home():
    return render_template("dashboard.html")


@app.route("/caregivers")
def caregivers():
    return render_template("caregivers.html")


@app.route("/matching")
def matching():

    caregivers = [
        {
            "name": "Maria Johnson",
            "skills": ["Personal Care", "Dementia"],
            "availability": "Mon-Fri",
            "location": "Philadelphia",
            "compliance": True
        },
        {
            "name": "James Williams",
            "skills": ["Companion Care", "Personal Care"],
            "availability": "Mon-Sat",
            "location": "Upper Darby",
            "compliance": True
        },
        {
            "name": "Angela Brown",
            "skills": ["Dementia", "Respite Care"],
            "availability": "Tue-Sun",
            "location": "Philadelphia",
            "compliance": False
        },
        {
            "name": "David Smith",
            "skills": ["Personal Care", "Mobility Support"],
            "availability": "Mon-Fri",
            "location": "Philadelphia",
            "compliance": True
        }
    ]

    required_skill = "Dementia"
    required_location = "Philadelphia"

    results = []

    for caregiver in caregivers:

        score, reasons = calculate_score(
            caregiver,
            required_skill,
            required_location
        )

        results.append({
            "name": caregiver["name"],
            "score": score,
            "reasons": reasons
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    return render_template(
        "matching.html",
        results=results,
        required_skill=required_skill,
        required_location=required_location
    )


@app.route("/schedule")
def schedule():

    shifts = [
        {
            "caregiver": "Maria Johnson",
            "client": "Client A",
            "date": "Monday",
            "time": "9:00 AM - 1:00 PM",
            "status": "Scheduled"
        },
        {
            "caregiver": "James Williams",
            "client": "Client B",
            "date": "Monday",
            "time": "10:00 AM - 2:00 PM",
            "status": "Scheduled"
        },
        {
            "caregiver": "David Smith",
            "client": "Client C",
            "date": "Tuesday",
            "time": "8:00 AM - 12:00 PM",
            "status": "Scheduled"
        }
    ]

    return render_template("schedule.html", shifts=shifts)


@app.route("/compliance")
def compliance():
    return render_template("compliance.html")


if __name__ == "__main__":
    app.run(debug=True)