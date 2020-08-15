import requests
from bs4 import BeautifulSoup


def del_space1(text: str):
    text_iter = iter(text)
    last_one = " "
    final_txt = ""
    for i in text_iter:
        if i.isspace():
            next_one = next(text_iter)
            if not next_one.isspace() or not last_one.isspace():
                final_txt += i + next_one
        else:
            final_txt += i
        last_one = i
    try:
        while final_txt[-1].isspace():
            final_txt = final_txt[0:-1]

        while final_txt[0].isspace():
            final_txt = final_txt[1:]
    except IndexError:
        pass
    return final_txt


def main():
    web = requests.get("https://m.one.co.il/Mobile/Live/Match.aspx?liveid=316548").content
    html_parser = BeautifulSoup(web, "html.parser")

    home_team = del_space1(html_parser.find("div", {"id": "mobile-live-home"}).text.replace("\n", "").replace("\r", ""))

    home_team_event = [i.text.replace("\n", "").replace("\r", "") for i in
                       html_parser.findAll("div", {"id": "mobile-live-home-events"})]
    home_team_event_lst = del_space1(home_team_event[0]).split("  ")

    ###
    guest_team = del_space1(html_parser.find("div", {"id": "mobile-live-guest"}).text.replace("\n",
                                                                                              "").replace("\r", ""))

    guest_team_event = [i.text.replace("\n", "").replace("\r", "") for i in
                        html_parser.findAll("div", {"id": "mobile-live-guest-events"})]
    guest_team_event_lst = del_space1(guest_team_event[0]).split("  ")

    ###

    result, status = (html_parser.find("span", {"id": "mobile-live-score"}).text,
                      html_parser.find("span", {"id": "mobile-live-status"}).text)
    chars = ' ' * (len(guest_team) + 2)
    print(f"{home_team}    vs    {guest_team}")
    print(chars + result)
    print(chars + status + "\n")

    while len(guest_team_event_lst) > len(home_team_event_lst):
        home_team_event_lst.append("")

    while len(guest_team_event_lst) < len(home_team_event_lst):
        guest_team_event_lst.append(" " * (len(home_team_event_lst[0]) + 2))

    home_event_iter = iter(home_team_event_lst)
    guest_event_iter = iter(guest_team_event_lst)
    for i in range(len(home_team_event_lst)):
        print(next(home_event_iter), next(guest_event_iter))


if __name__ == '__main__':
    main()
