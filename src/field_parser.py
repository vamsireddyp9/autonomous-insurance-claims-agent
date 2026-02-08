import re

def parse_fields(text):
    def find(pattern):
        match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
        return match.group(1).strip() if match else None

    fields = {
        # Policy Information
        "policy_number": find(r"POLICY\s+NUMBER\s+([A-Z0-9\-]+)"),
        "policyholder_name": find(r"NAME OF INSURED.*?\n([A-Z ,]+)"),
        "effective_dates": None,  # Not present in template

        # Incident Information
        "incident_date": find(r"DATE OF LOSS.*?(\d{2}/\d{2}/\d{4})"),
        "incident_time": find(r"TIME\s+([0-9: ]+(AM|PM))"),
        "location": find(r"LOCATION OF LOSS.*?\n(.+)"),
        "description": find(r"DESCRIPTION OF ACCIDENT.*?\n(.+)"),

        # Involved Parties
        "claimant": None,
        "third_parties": None,
        "contact_details": None,

        # Asset Details
        "asset_type": "vehicle",
        "asset_id": find(r"V\.?I\.?N\.?\s*[:\-]?\s*([A-Z0-9]+)"),
        "estimated_damage": None,

        # Other Mandatory Fields
        "claim_type": "auto",
        "attachments": None,
        "initial_estimate": None
    }

    # Try extracting estimate if present
    damage_match = re.search(r"ESTIMATE\s+AMOUNT\s+\$?([0-9,]+)", text)
    if damage_match:
        fields["estimated_damage"] = int(damage_match.group(1).replace(",", ""))
        fields["initial_estimate"] = fields["estimated_damage"]

    return fields
