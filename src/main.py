import json
from src.extractor import extract_text_from_pdf
from src.field_parser import parse_fields
from src.validator import find_missing_and_inconsistent

from src.router import route_claim

def process_fnol(file_path):
    text = extract_text_from_pdf(file_path)
    fields = parse_fields(text)
    missing, inconsistent = find_missing_and_inconsistent(fields)
    route, reason = route_claim(fields, missing)

    return {
        "extractedFields": fields,
        "missingFields": missing,
        "recommendedRoute": route,
        "reasoning": reason
    }

if __name__ == "__main__":
    result = process_fnol("data/sample_fnol.pdf")
    print(json.dumps(result, indent=2))
