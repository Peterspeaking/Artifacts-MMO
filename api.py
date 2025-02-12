import requests
import os
from dotenv import load_dotenv

load_dotenv()

class ArtifactAPI:
    BASE_URL = "https://api.artifactsmmo.com"

    def __init__(self, character: str):
        self.token =  os.getenv("TOKEN")
        self.character = character
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {self.token}",
        }
    
    def _get(self, data: dict = None):
        """
        Internal helper method to GET character data.
        """
        url = f"{self.BASE_URL}/my/{self.character}"
        try:
            response = requests.get(url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json().get("data")
        except requests.exceptions.RequestException as error:
            return None

    def _post(self, endpoint: str, data: dict = None):
        """
        Internal helper method to POST to a given endpoint.
        """
        url = f"{self.BASE_URL}/my/{self.character}/action/{endpoint}"
        print(url)
        try:
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json().get("data")
        except requests.exceptions.RequestException as error:
            print(f"Error calling endpoint '{endpoint}': {error}")
            return None

    def fight(self):
        """Call the fight endpoint."""
        return self._post("fight")

    def move(self, x: int, y: int):
        """Call the move endpoint with x, y coordinates."""
        return self._post("move", data={"x": x, "y": y})

    def rest(self):
        """Call the rest endpoint."""
        return self._post("rest", data={})
    
    def equip(self, code: str, slot: str):
        """Call the equip endpoint with code and slot to equip."""
        return self._post("rest", data={"code": code, "slot": slot})
    
    def unequip(self, slot: str):
        """Call the unequip endpoint with slot to unequip."""
        return self._post("rest", data={"slot": slot})

    def gathering(self):
        """Call the gathering endpoint."""
        return self._post("gathering")
    
    def crafting(self, code: str, quantity: int):
        """Call the crafting endpoint with code and quantity to craft."""
        return self._post("crafting", data={"code": code, "quantity": quantity})
    
    def deposit(self, code: str, quantity: int):
        """Call the deposit endpoint with code and quantity to deposit."""
        return self._post("bank/deposit", data={"code": code, "quantity": quantity})
    
    def get_inventory(self):
        """Get the character's inventory."""
        return self._get()