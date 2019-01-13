import json
import os

from bs4 import BeautifulSoup


def parse_top_250(data, path):
    filmsLibrary = dict()

    soup = BeautifulSoup(data.text, 'html.parser')
    count = 0
    ratings = soup.findAll("td", class_="imdbRating")
    if (os.path.exists(path)): os.remove(path)
    for quote in soup.findAll("td", class_="titleColumn"):
        filmInfo = dict()
        filmInfo["Position"] = quote.text.split("\n")[1].replace(" ", "")[:-1]
        filmInfo["Year"] = quote.span.text[1:-1]
        filmInfo["Director"] = quote.a["title"].split(r"dir.")[0][:-2]
        filmInfo["Crew"] = quote.a["title"].split(r"dir.")[1][3:]
        filmInfo["Rating"] = ratings[count].text[1:-1]
        filmsLibrary[quote.a.text] = filmInfo
        count += 1

        my_json = json.JSONEncoder(skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True,
                                   sort_keys=False, indent=None, separators=None, default=None).encode(filmsLibrary)
    write_json(path, my_json)


def write_json(path, my_json):
    try:
        print("Start to write file - " + path)
        my_file = open(path, "w")
        for index in my_json:
            my_file.write(index)
        my_file.close()
    except FileNotFoundError:
        print("File not found")
