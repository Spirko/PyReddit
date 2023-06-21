import os
import json
def read_secrets() -> dict:
    filename = os.path.join('secrets.json')
    try:
        with open(filename, mode='r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}

if __name__ == "__main__":
  
  print("Reading secrets.json")
  secrets = read_secrets()
  
  print(f"Reddit username: {secrets['USERNAME']}")
  print(f"Reddit app ID: {secrets['SCRIPT_ID']}")