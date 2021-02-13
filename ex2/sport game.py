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
    test_get_game_info()
    HTML = requests.get("https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316548").content
    print(get_game_info(HTML))
