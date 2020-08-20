from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


class Datetime:
    def __init__(self, year, month, day, hours, minutes, seconds, neme_day=None, name_month=None):
        self._year = year
        self._month = month
        self._day = day
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        self._name_day = neme_day
        self._name_month = name_month

    def __str__(self):
        return " ".join([f"{str(self._year)}-{str(self._day)}-{str(self._month)}",
                         f"{self._hours}:{self._minutes}:{self._seconds}", str(self._name_month), str(self._name_day)])

    @staticmethod
    def now():
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]

        html_page = BeautifulSoup(urlopen("https://www.timeanddate.com/worldclock/israel/jerusalem").read(),
                                  "html.parser")

        h, m, s = re.findall(r'(\d+):(\d+):(\d+)', html_page.body.find("span", {"id": "ct"}).text)[0]

        day_name, month_name, day_num, year = \
            re.findall(r'(\w+), (\w+) (\d{1,2}), (\d{4})', html_page.find("span", {"id": "ctdat"}).text)[0]

        datetime_obg = Datetime(year, months.index(month_name) + 1, day_num, h, m, s, day_name, month_name)
        datetime_obg.zone_time = lambda: html_page.tbody.tr.a.text
        return datetime_obg

    def str_time(self, part):
        str_dct = {"%Y": self._year, "%m": self._month, "%D": self._day, "%H": self._hours, "%M": self._minutes,
                   "%S": self._seconds, "%A": self._name_day, "%a": self._name_day[0:3], "%B": self._name_month,
                   "%b": self._name_month[0:3]}
        return str_dct[part]

    def time(self) -> str:
        return f"{self._hours}:{self._minutes}:{self._seconds}"

    def date(self) -> str:
        return f"{self._year}-{self._month}-{self._day}"


if __name__ == '__main__':
    exam = Datetime.now()
    print(exam.zone_time())
