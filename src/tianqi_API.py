import requests


def re(canshu):
    url = "http://wthrcdn.etouch.cn/weather_mini"
    canshu = {"city": canshu}
    re = requests.get(url=url, params=canshu)
    html = re.json()
    return html
