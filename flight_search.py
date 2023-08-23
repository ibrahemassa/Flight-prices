import requests
import datetime as dt
from dateutil.relativedelta import relativedelta

header = {
    "apikey": "tequila API KEY"
}

today = dt.datetime.now().date()
after_six = today + relativedelta(months=+6)

class FlightSearch:
    def __init__(self, destination):
        self.flights_parameters = {
            "fly_from": "LON",
            "fly_to": destination,
            "date_from": today.strftime("%d/%m/%Y"),
            "date_to": after_six.strftime("%d/%m/%Y"),
            "one_per_date": 1,
            "adults": 1,
            "price_to": "",
            "curr": "GBP",
            "children": 0,
            "selected_cabins": "M",
            "max_stopovers": 0
}
        self.flights_response = requests.get("https://api.tequila.kiwi.com/v2/search", params = self.flights_parameters, headers= header)
        self.flights_response.raise_for_status()
        self.data = self.flights_response.json()

