#!/usr/bin/env python3
import json
import requests
from datetime import datetime
import os
cwd = os.getcwd()

with open(cwd+"/data.json", "r") as settings:
    settings = json.load(settings)


def urlprobe(r, url):
    try:
        response = r.get(url)
        if response.status_code == 200:
            return True
        else:
            print("response %s" % response.status_code)
            return False
    except:
        print("Invalid URL")
        return False


def addProductTocart(url, data):
        datas = {
            "product_id": data[0],
            "quantity": data[1]
            }
        res = r.post(url, data=datas)
        print(json.loads(res.text))
        return res


if __name__ == "__main__":
    base_url = settings["base_url"]
    products = settings["products"]
    links = settings["links"]
    userdata = settings["userdata"]
    headers = {
        'User-Agent': \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/91.0.4472.77 Safari/537.36" \
        }

    r = requests.Session()
    r.headers.update(headers)

    if urlprobe(r, base_url):
        for product in products:
            # print(product)
            cart_url = base_url + settings["add_product_url"]
            print(cart_url)
            addProductTocart(cart_url, product)
        for link in links:
            print(link)
            url = base_url+link[0]
            if link[1].upper() == "GET":
                r.get(url)
            elif link[1].upper() == "POST":
                res = r.post(url, data=userdata)
                # print(json.loads(res.text))
            elif link[1].upper() == "TIME":
                now = str(int(datetime.now().timestamp()))
                url = url % now
                r.get(url)
    else:
        print("Somthing went wrong!")
