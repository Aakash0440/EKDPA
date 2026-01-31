def evaluate_knowledge_risk(
    documentation_coverage: int,
    knowledge_owner_count: int,
    role_criticality: str
):
    """
    Evaluates organizational knowledge risk.
    Returns HIGH, MEDIUM, or LOW.
    """

    if role_criticality == "HIGH":
        if documentation_coverage < 50 and knowledge_owner_count <= 1:
            return "HIGH"
        elif documentation_coverage < 70:
            return "MEDIUM"
        else:
            return "LOW"

    if role_criticality == "MEDIUM":
        if documentation_coverage < 40:
            return "MEDIUM"
        else:
            return "LOW"

    return "LOW"


if __name__ == "__main__":
    # Demo run
    risk = evaluate_knowledge_risk(
        documentation_coverage=25,
        knowledge_owner_count=1,
        role_criticality="HIGH"
    )
    print("Risk Level:", risk)
