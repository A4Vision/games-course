import requests
from bs4 import BeautifulSoup


def get_game_info(html_text) -> dict:
    """
    :param html_text:
    :return: return the home team, guest team and the game result in dictionary
    """
    html_parser = BeautifulSoup(html_text, "html.parser")
    global home, guest, result, status
    home = html_parser.find("div", {"id": "mobile-live-home"}).text.replace("\n", "").replace("\r", "").strip()
    guest = html_parser.find("div", {"id": "mobile-live-guest"}).text.replace("\n", "").replace("\r", "").strip()

    result = html_parser.find("span", {"id": "mobile-live-score"}).text
    status = html_parser.find("span", {"id": "mobile-live-status"}).text
    return {"home team": home, "guest team": guest, "result": result, "status": status}


def test_get_game_info():
    with open(r"../files/html_exam_text.txt") as f:
        get_game_info(f.read())
    assert home == "ברצלונה"
    assert guest == "באיירן מינכן"
    assert result == "8 - 2"


def create_csv(urls_lst):
    with open(r"../files/sport_games.csv", "w") as file:
        file.write("קבוצה אורחת, תוצאה\\שעת המשחק, קבוצה ביתית\n")
        for i in urls_lst:
            html = requests.get(i).content
            get_game_info(html)

            file.write(f"{home}, {result}, {guest}\n")


if __name__ == '__main__':
    urls_of_games = ["https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316639",
                     "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316641",
                     "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316583",
                     "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316584",
                     "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316582",
                     "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316581",
                     "https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316643"]
    create_csv(urls_of_games)
