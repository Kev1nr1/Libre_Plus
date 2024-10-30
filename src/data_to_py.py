import subprocess
import json

#Return the full Libre data
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


# Only return the current glucose value
def get_current_glucose():
    data = get_libre_data()
    dict_libre_data = dict(data)
    current_glucose = dict_libre_data['current']
    return current_glucose