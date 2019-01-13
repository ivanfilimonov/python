import json
import os
import re
import time

import boto.s3
import requests
from boto.s3.key import Key


def upload_log_to_s3():
    f = ""
    s3_connection = ""
    prop = open(os.getcwd() + "\\prop.json", "r")
    properties = json.load(prop)
    prop.close()

    try:
        s3_connection = boto.connect_s3(properties["KEY"], properties["SECRET_KEY"], host = properties["HOST"])
        bucket = s3_connection.get_bucket('python-final')
        key = Key(bucket, 'log.log')
        key.size = os.path.getsize(os.getcwd() + "\\log.log")
        f = open(os.getcwd() + "\\log.log", 'r')
        key.send_file(f)
    except BaseException:
        print("file uploaded and I really have no idea why mistake appears here")
    finally:
        if(s3_connection is not ""):
            s3_connection.close()
        if (f is not ""):
            f.close()

def run_full_console_scenario():
    continue_loop = True
    while (continue_loop):
        print("\nWrite <link for request + 1 space symbol> or type B to close process")
        link = input()
        if (link == "B"):
            break
        else:
            get_tags(link)
        if (os.path.exists("log.log")):
            print("\nDo you want push your log file to s3 bucket? Press Y to do it")
            link = input()
            if (link == "Y"):
                upload_log_to_s3()
        print("\nDo you want research another link? Press Y to do it again")
        link = input()
        if (link != "Y"):
            print("\nSee you soon, my friend!\n")
            break


def get_tags(link):
    try:
        tagsCalculator = dict()
        count = 0
        res = requests.get(link, headers={"Accept-Language": "En-us"})
        for tag in re.findall(r"</(\w+)>", str(res.text)):
            count += 1
            if (tagsCalculator.keys().__contains__(tag)):
                tagsCalculator[tag] += 1
            else:
                tagsCalculator[tag] = 1
        result = "{0}_____link={1}_____number_of_tags={2}_____details={3}".format(time.ctime(), link, count,
                                                                                  tagsCalculator)
        write_log(result)
    except BaseException:
        print("Bad link: <{0}>".format(link))


def write_log(data):
    try:
        print("Start to write log")
        my_file = open("log.log", "w")
        for index in data:
            my_file.write(str(index))
        my_file.close()
        print(data)
    except FileNotFoundError:
        print("File not found")
