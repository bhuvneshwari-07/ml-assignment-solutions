# Scenario 9: Structured Response Generation
# Task: Generate a JSON response using an API for a given query
# and handle cases where the response is not valid JSON.

import json

def generate_json_response():
    # Replace this with actual Gemini API call if needed
    response = '{"benefits": ["Easy to learn", "Rich libraries", "Strong community"]}'

    try:
        parsed = json.loads(response)
        return parsed
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response"}


if __name__ == "__main__":
    print(generate_json_response())