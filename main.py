# -*- coding:utf-8 -*-

import requests
import folium
from pyfiglet import Figlet


def get_by_ip(ip="127.0.0.1"):
    preview = Figlet(font="slant")
    print(preview.renderText("INFO BY IP"))
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        date = {
            "[IP]": response.get("query"),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Index]': response.get('zip'),
            '[Country]': response.get('country'),
            '[City]': response.get('city'),
            '[Region]': response.get('regionName')
        }

        for i, x in date.items():
            print(i, x, sep=" - ")

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("city")}_{response.get("query")}.html')

    except requests.exceptions.ConnectionError:
        print("[!] Please check your connection!")


def main():
    get_by_ip(input("Press your IP address: "))


if __name__ == "__main__":
    main()
