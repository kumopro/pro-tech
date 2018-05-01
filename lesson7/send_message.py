import requests

def send_message():
    url = "https://maker.ifttt.com/trigger/"
    event_name = "come_home"
    key = ""
    webhook_url = url + event_name + "/with/key/" + key
    print(webhook_url)
    contents = {'value1':'あああ', 'value2':'いいい', 'value3':'ううう'}
    requests.post(webhook_url, json=contents)
