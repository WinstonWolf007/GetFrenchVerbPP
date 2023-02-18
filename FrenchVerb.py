import urllib.request as url_req
from bs4 import BeautifulSoup


def get_pp_french_verb(infinitive_verb: str) -> list:
    url = f"https://leconjugueur.lefigaro.fr/conjugaison/verbe/{infinitive_verb}.html"

    request = url_req.urlopen(url)
    allVerb = []

    if request.getcode() == 200:
        html_code = BeautifulSoup(str(request.read()), features="html.parser")
        try:
            getPPSection = html_code.find_all("div", class_="conjugBloc")[21]  # index of pp section in page
        except IndexError:
            print("\033[91mInvalid verb\033[0m")
            return []

        # html_code2 = BeautifulSoup(str(getPPSection), features="html.parser")
        verbStruc = ""
        first = True
        for el in getPPSection:
            if first:
                first = False
            else:
                if str(el) == "<br/>" or str(el) == "<br>":
                    allVerb.append(verbStruc)
                    verbStruc = ""
                else:
                    verbStruc += str(el).replace("<b>", "").replace("</b>", "")
        return allVerb


    else:
        print("Err:", request.getcode())
        return []
