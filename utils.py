import json
from dotenv import load_dotenv
from os import environ as env
load_dotenv()

data = json.load(open(env.get("CRED_FILE")))

with open(".env", "w") as file:
    for key,value in data.items():
        file.write(f"{key.upper()} = '{value}'\n")
