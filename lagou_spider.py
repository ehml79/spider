
import uuid
import requests

def get_uuid():
    return str(uuid.uuid4())

def get_lagou(page):
    url = "https://www.lagou.com/jobs/positionAjax.json"
    # querystring = {"px": "new", "city": "广州", "needAddtionalResult": "false", "isSchoolJob": "0"}
    querystring = {"city": "广州", "needAddtionalResult": "false"}
    payload = "first=false&pn=" + str(page) + "&kd=Python"

    cookie = "JSESSIONID=" + get_uuid() + ";" \
        "user_trace_token=" + get_uuid() + "; LGUID=" + get_uuid() + "; index_location_city=%E6%88%90%E9%83%BD; " \
        "SEARCH_ID=" + get_uuid() + '; _gid=GA1.2.717841549.1514043316; ' \
        '_ga=GA1.2.952298646.1514043316; ' \
        'LGSID=' + get_uuid() + "; " \
        "LGRID=" + get_uuid() + "; "

    headers = {
        'cookie': cookie,
        'origin': "https://www.lagou.com",
        'x-anit-forge-code': "0",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.8,en;q=0.6",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
        'accept': "application/json, text/javascript, */*; q=0.01",
        'referer': "https://www.lagou.com/jobs/list_Java?px=new&city=%E6%88%90%E9%83%BD",
        'x-requested-with': "XMLHttpRequest",'connection': "keep-alive",
        'x-anit-forge-token': "None",'cache-control': "no-cache",
        'postman-token': "91beb456-8dd9-0390-a3a5-64ff3936fa63"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    print(response.text)

if __name__ == "__main__":
    for n in range(0, 1):
        get_lagou(n)
        # time.sleep(5)
