import requests

header = {
    "Authorization": "SHEETY key"
}

class DataManager:
    def __init__(self):
        self.sheety_response = requests.get("SHEETY ENDPOINT", headers= header)
        self.sheety_response.raise_for_status()
        self.data = self.sheety_response.json()

    def get_cities(self):
        return [{"code": city["iataCode"], "lowest_price": city["lowestPrice"]} for city in self.data["prices"]]
    

