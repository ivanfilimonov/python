import json
from unittest import TestCase

import requests

from main.hw5.top250 import parse_top_250


class TestParseTop250(TestCase):

    def test_parse_top_250(self):
        link = "https://imdb.com/chart/top"
        res = requests.get(link, headers={"Accept-Language": "En-us"})
        parse_top_250(res, "top250.json")
        with open("top250.json") as result_json:
            result_data: list = json.load(result_json)
            print(result_data)
            self.assertEqual(result_data["The Shawshank Redemption"],
                             {"Position": "1", "Year": "1994", "Director": "Frank Darabont",
                              "Crew": "Tim Robbins, Morgan Freeman", "Rating": "9.2"})

            self.assertEqual(result_data["The Godfather"],
                             {"Position": "2", "Year": "1972", "Director": "Francis Ford Coppola",
                              "Crew": "Marlon Brando, Al Pacino", "Rating": "9.2"})

            self.assertEqual(result_data["Goodfellas"],
                             {"Position": "17", "Year": "1990", "Director": "Martin Scorsese",
                              "Crew": "Robert De Niro, Ray Liotta", "Rating": "8.7"})
