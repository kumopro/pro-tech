import requests

def send_message():
    url = "https://maker.ifttt.com/trigger/"
    event_name = "taro_come_home"
    key = ""
    webhook_url = url + event_name + "/with/key/" + key
    print(webhook_url)
    contents = {'value1':'鈴木', 'value2':'太郎', 'value3':'テスト'}
    requests.post(webhook_url, json=contents)
