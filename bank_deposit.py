import time
from api import ArtifactAPI
import json

if __name__ == "__main__":
    character = "MrSpeak"
    api = ArtifactAPI(character)
    result = api.deposit("sap", 3)
    print(json.dumps(result, indent=2))