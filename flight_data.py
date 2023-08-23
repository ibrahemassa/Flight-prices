import requests
from data_manager import DataManager
from flight_search import FlightSearch



class FlightData:
    def __init__(self):
        data_manager = DataManager()
        self.cities = [city["code"] for city in data_manager.get_cities()]

    def get_prices(self):
        lowest_prices = []
        for city in self.cities:
            flight = FlightSearch(city)
            data = flight.data["data"]
            maxi = data[0]["price"]
            index = data[0]
            for fly in data:
                if fly["price"] > maxi:
                    maxi = fly["price"]
                    index = fly
            lowest_prices.append(index)
        return lowest_prices
