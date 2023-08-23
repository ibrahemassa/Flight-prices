import requests

header = {
    "Authorization": "Bearer asdgyuias667t68"
}

class DataManager:
    def __init__(self):
        # sheety_response = requests.put("https://api.sheety.co/a2ccf90bd6fe726e5b3e13a9cd5d9f3b/flightDeals/prices/[Object ID]")
        self.sheety_response = requests.get("https://api.sheety.co/a2ccf90bd6fe726e5b3e13a9cd5d9f3b/flightDeals/prices", headers= header)
        self.sheety_response.raise_for_status()
        self.data = self.sheety_response.json()

    def get_cities(self):
        return [{"code": city["iataCode"], "lowest_price": city["lowestPrice"]} for city in self.data["prices"]]
    

