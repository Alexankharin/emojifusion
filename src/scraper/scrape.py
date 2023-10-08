import json
import urllib
import numpy as np
import re
import tqdm
import git
import os

repo = git.Repo(".", search_parent_directories=True)
root = repo.working_tree_dir


def download_site():
    url = "https://emojikitchen.dev/assets/index-39d501e3.js"
    urllib.request.urlretrieve(url, os.path.join(root, "data/emojisite.json"))
    url = "https://emojikitchen.dev"
    urllib.request.urlretrieve(url, os.path.join(root, "/data/emojisite.html"))
    return 0


def get_blended():
    rawdata = open("../data/emojisite.json").read()
    # modified_json_str = add_quotes_to_ints_and_words(rawdata)
    # find the patterns
    pattern = r'"https://www\.gstatic\.com/android/keyboard/emojikitchen/2[^"]+"'
    # data=json.loads(modified_json_str)
    alllinks = re.findall(pattern, rawdata)
    alllinks.sort()
    onlynew = {}
    for link in alllinks:
        name = link.split("/")[-1][:-1]
        onlynew[name] = link[1:-1]
    for name, url in tqdm.tqdm(onlynew.items()):
        try:
            urllib.request.urlretrieve(url, f"../data/emojis/blended/{name}")
        except:
            print("failed ", url)
    return 0


def get_original():
    rawdata = open("../data/emojisite.json").read()
    # modified_json_str = add_quotes_to_ints_and_words(rawdata)
    # find the patterns
    pattern = r'"https://www\.gstatic\.com/android/keyboard/emojikitchen/2[^"]+"'
    # data=json.loads(modified_json_str)
    alllinks = re.findall(pattern, rawdata)
    alllinks.sort()
    onlynew = {}
    for link in alllinks:
        name = link.split("/")[-1][:-1]
        onlynew[name] = link[1:-1]
    todownload = set()
    for name in onlynew.keys():
        todownload.add(name.split(".")[0].split("_")[0])
        todownload.add(name.split(".")[0].split("_")[1])
        todownload = list(todownload)
    for name in tqdm.tqdm(todownload):
        url = f"https://raw.githubusercontent.com/googlefonts/noto-emoji/main/svg/emoji_{name}.svg"
        try:
            urllib.request.urlretrieve(url, f"../data/emojis/bare/{name}.svg")
        except:
            print("failed ", url)
    return 0
