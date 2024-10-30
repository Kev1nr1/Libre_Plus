import subprocess
import json

def get_libre_data():
    # Run the Node.js script and capture the output
    result = subprocess.run(
        ['node', 'fetch_libre_data.js'],
        capture_output=True,
        text=True
    )
    
    # Check for errors
    if result.returncode != 0:
        print("Error:", result.stderr)
        return None

    # Parse the JSON output
    try:
        data = json.loads(result.stdout)
        return data
    except json.JSONDecodeError:
        print("Failed to parse JSON:", result.stdout)
        return None

# Fetch and print the data
libre_data = get_libre_data()
print("Libre Data:", libre_data)