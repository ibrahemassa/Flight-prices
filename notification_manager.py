import smtplib
import requests

header = {
    "Authorization": "SHEETY KEY"
}

class NotificationManager:
    def __init__(self, city, price, date):
        self.city = city
        self.price = price
        self.date = date
        self.users = self.get_users()
        self.message = f"Price down for flight from LON to {self.city}.\nthe new price is {self.price}GBP.\ndate: {self.date}\n\nBest,\nFlights agency.\n"


    def send_message(self, email: str):
        my_email = "YOUR EMAIL"
        password = "YOUR PASSWORD"

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
        self.response = requests.get("SHEETY ENDPOINT", headers= header)
        self.response.raise_for_status()
        self.data = self.response.json()
        return self.data["users"]