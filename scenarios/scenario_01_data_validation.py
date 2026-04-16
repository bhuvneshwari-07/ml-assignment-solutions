# Scenario 1: Data Validation
# Task: Validate a list of dictionaries and ensure the 'age' field contains integer values.

def validate_data(data):
    invalid_entries = []

    for entry in data:
        if "age" not in entry or not isinstance(entry["age"], int):
            invalid_entries.append(entry)

    return invalid_entries


if __name__ == "__main__":
    data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": "25"}]
    print("Invalid Entries:", validate_data(data))