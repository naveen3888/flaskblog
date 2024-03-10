import json

# Load service account credentials from JSON file
def load_credentials():
    with open('E\\blog\\cloud.json', 'r') as f:
        credentials = json.load(f)
    return credentials

# Print loaded credentials
print(load_credentials())
