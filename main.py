from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager
import requests


# flights = FlightSearch("IST")
# print(len(flights.data["data"]))

data_manager = DataManager()

cities = data_manager.get_cities()

flight_data = FlightData()
prices = flight_data.get_prices()

lowest_cites_prices = []

for i in range(0, len(cities)):
    if prices[i]["price"] < cities[i]["lowest_price"]:
        dicti = {
            "city": cities[i]["code"],
            "lowest price": prices[i]["price"],
            "date": prices[i]["utc_departure"]
        }
        lowest_cites_prices.append(dicti)

min_price = 99999
for city in lowest_cites_prices:
    if city["lowest price"] < min_price:
        min_price = city["lowest price"]
        lowest_city = city["city"]
        date = city["date"]

noti = NotificationManager(lowest_city, min_price, date)
emails = [user["email"] for user in noti.users]
for email in emails:
    noti.send_message(email)





