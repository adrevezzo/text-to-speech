import json
from dotenv import load_dotenv

data = json.load(open('key.json'))

with open(".env", "w") as file:
    for key,value in data.items():
        file.write(f"{key.upper()} = '{value}'\n")
