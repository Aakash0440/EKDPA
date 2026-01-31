from evaluate_knowledge_risk import evaluate_knowledge_risk

def orchestrate_knowledge_guardian_flow(inputs):
    risk = evaluate_knowledge_risk(
        inputs["documentation_coverage"],
        inputs["knowledge_owner_count"],
        inputs["role_criticality"]
    )

    if risk == "HIGH":
        return {
            "status": "IN_PROGRESS",
            "action": "Trigger knowledge capture workflow",
            "next_steps": [
                "Request documentation",
                "Schedule peer validation",
                "Assign backup owner"
            ]
        }

    return {
        "status": "SECURED",
        "action": "Log low risk",
        "next_steps": []
    }


if __name__ == "__main__":
    demo_input = {
        "employee_name": "Ali Khan",
        "role_criticality": "HIGH",
        "documentation_coverage": 25,
        "knowledge_owner_count": 1
    }

    result = orchestrate_knowledge_guardian_flow(demo_input)
    print(result)
