from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


class Datetime:
    _html_page = BeautifulSoup(urlopen("https://www.timeanddate.com/worldclock/israel/jerusalem").read(), "html.parser")
    
    def __init__(self, year, month, day, hours, minutes, seconds, neme_day=None, name_month=None):
        self._year = year
        self._month = month
        self._day = day
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        self._neme_day = neme_day
        self._name_month = name_month

    def __str__(self):
        return " ".join([f"{str(self._year)}-{str(self._day)}-{str(self._month)}",
                         f"{self._hours}:{self._minutes}:{self._seconds}", str(self._name_month) , str(self._neme_day)])

    @staticmethod
    def now():
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]

        html_page = Datetime._html_page

        h, m, s = re.findall(r'(\d+):(\d+):(\d+)', html_page.body.find("span", {"id": "ct"}).text)[0]

        day_name, month_name, day_num, year = \
            re.findall(r'(\w+), (\w+) (\d{1,2}), (\d{4})', html_page.find("span", {"id": "ctdat"}).text)[0]

        return Datetime(year, months.index(month_name) + 1, day_num, h, m, s, day_name, month_name)

    def strftime(self, part):
        strf_dct = {"%Y": self._year, "%m": self._month, "%D": self._day, "%H": self._hours, "%M": self._minutes,
                    "%S": self._seconds, "%A": self._neme_day, "%a": self._neme_day[0:3], "%B": self._name_month,
                    "%b": self._name_month[0:3]}
        return strf_dct[part]

    @staticmethod
    def zone_time() -> str:
        html_page = Datetime._html_page
        return html_page.tbody.tr.a.text

    def time(self) -> str:
        return f"{self._hours}:{self._minutes}:{self._seconds}"

    def date(self) -> str:
        return f"{self._year}-{self._month}-{self._day}"


if __name__ == '__main__':
    exam = Datetime.now()
