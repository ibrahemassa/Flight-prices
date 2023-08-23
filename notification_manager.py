import smtplib
import requests

header = {
    "Authorization": "Bearer asdgyuias667t68"
}

class NotificationManager:
    def __init__(self, city, price, date):
        self.city = city
        self.price = price
        self.date = date
        self.users = self.get_users()
        self.message = f"Price down for flight from LON to {self.city}.\nthe new price is {self.price}GBP.\ndate: {self.date}\n\nBest,\nFlights agency.\n"


    def send_message(self, email: str):
        my_email = "ibrahem.fares204@gmail.com"
        password = "loglbbcevoqsmhqo"

        with smtplib.SMTP(host = "smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user = my_email, password = password)
            connection.sendmail(
                from_addr = my_email,
                to_addrs = email,
                msg = f"Subject:Flight alert!\n\n{self.message}"
            )
            connection.close()

    def get_users(self):
        self.response = requests.get("https://api.sheety.co/a2ccf90bd6fe726e5b3e13a9cd5d9f3b/flightDeals/users", headers= header)
        self.response.raise_for_status()
        self.data = self.response.json()
        return self.data["users"]