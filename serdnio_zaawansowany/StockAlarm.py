import datetime
import time
import winsound

import requests
from bs4 import BeautifulSoup

from serdnio_zaawansowany.FileManipulation import FileManipulation


class StockAlarm():
    interval = 10 * 60
    url = "https://www.gpw.pl/spolka?isin=LU2237380790"
    old_price = 0

    def __init__(self):
        today = datetime.date.today()
        self.file_manipulation = FileManipulation(f"Allegro_{today.strftime('%d_%m_%Y')}")
        while True:
            self.get_data()
            time.sleep(self.interval)

    def get_data(self):
        try:
            request = requests.get(self.url)
        except:
            print("Błąd wczytywania danych. ")
        else:
            soup = BeautifulSoup(request.text, 'html.parser')
            try:
                share_price = soup.find("span", {"class", "summary"}).string
            except:
                print("Nie udało się znaleźć ceny akcji.")
            else:
                self.analysis(float(share_price.replace(',', '.')))

    def analysis(self, share_price):
        if self.old_price > 0:
            percentage_change = (self.old_price - share_price) / self.old_price
            if percentage_change > 1:
                self.buy_alert()
            elif percentage_change < -1:
                self.sell_alert()
            self.print_info(share_price, percentage_change)
        self.old_price = share_price

    @staticmethod
    def buy_alert():
        for i in range(5):
            winsound.MessageBeep(type=winsound.MB_OK)
            time.sleep(0.2)

    @staticmethod
    def sell_alert():
        for i in range(5):
            winsound.MessageBeep(type=winsound.MB_ICONHAND)
            time.sleep(0.5)

    def print_info(self, share_price, percentage_change):
        date = str(datetime.datetime.now()).split('.')[0]
        info = f"{date} {share_price}, {percentage_change}%"
        print(info)
        self.file_manipulation.add_line(info)




stock_alarm = StockAlarm()
