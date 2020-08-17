import re
import requests
from bs4 import BeautifulSoup


def get_game_info(html_text):
    """
    :param html_text:
    :return: return the home team, guest team and the game result
    """
    html_parser = BeautifulSoup(html_text, "html.parser")
    home = html_parser.find("div", {"id": "mobile-live-home"}).text.replace("\n", "").replace("\r", "").strip()
    guest = html_parser.find("div", {"id": "mobile-live-guest"}).text.replace("\n", "").replace("\r", "").strip()

    result = html_parser.find("span", {"id": "mobile-live-score"}).text
    status = html_parser.find("span", {"id": "mobile-live-status"}).text
    return f"{guest}   {result}   {home}\n{' ' * (len(home) + 1)} {status}"


def test_get_game_info():
    html_text = requests.get("https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316548").content
    func_info = get_game_info(html_text)
    assert "ברצלונה" in func_info
    assert "באיירן מינכן" in func_info
    assert "8 - 2" in func_info


if __name__ == '__main__':
    games_lst = ["https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316639",
                 "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316641",
                 "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316583",
                 "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316584",
                 "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316582",
                 "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316581",
                 "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316643",
                 "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316592",
                 "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316590",
                 "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316589",
                 "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316588",
                 "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316566",
                 "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316593",
                 "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316591",
                 "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316587",
                 "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316586",
                 "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316688",
                 "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316552",
                 "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316579",
                 "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316580",
                 "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316559"]

    file = open("sport_games.csv", "w")
    file.write("קבוצה אורחת, תוצאה\\שעת המשחק, קבוצה ביתית\n")
    for i in games_lst:
        html = requests.get(i).content
        game_info = get_game_info(html)
        
        result = re.search(r"\d+\s*.\s*\d+", game_info).group()
        home, guest = [j.replace("\n", "").replace("הסתיים", "").strip() for j in re.split(r"\d+\s*.\s*\d+", game_info)]
        file.write(f"{guest}, {result}, {home}\n")
    file.close()
