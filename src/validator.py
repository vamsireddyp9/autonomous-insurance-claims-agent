MANDATORY_FIELDS = [
    "policy_number",
    "policyholder_name",
    "incident_date",
    "location",
    "description",
    "claim_type"
]

LABEL_KEYWORDS = [
    "DATE", "NAME", "ADDRESS", "CONTACT", "INSURED", "OWNER", "VEHICLE", "STREET"
]

def find_missing_and_inconsistent(fields):
    missing = []
    inconsistent = []

    for field in MANDATORY_FIELDS:
        value = fields.get(field)

        if not value:
            missing.append(field)
        else:
            if any(keyword in value.upper() for keyword in LABEL_KEYWORDS):
                inconsistent.append(field)

    return missing, inconsistent
