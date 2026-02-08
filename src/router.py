def route_claim(fields, missing_fields):
    description = (fields.get("description") or "").lower()
    damage = fields.get("estimated_damage")
    claim_type = (fields.get("claim_type") or "").lower()

    if missing_fields:
        return (
            "Manual Review",
            f"Missing mandatory fields: {', '.join(missing_fields)}"
        )

    if any(word in description for word in ["fraud", "staged", "inconsistent"]):
        return (
            "Investigation Flag",
            "Suspicious keywords found in description"
        )

    if claim_type == "injury":
        return (
            "Specialist Queue",
            "Injury-related claim"
        )

    if damage is not None and damage < 25000:
        return (
            "Fast-track",
            "Estimated damage below 25,000"
        )

    return (
        "Manual Review",
        "Does not meet fast-track criteria"
    )
