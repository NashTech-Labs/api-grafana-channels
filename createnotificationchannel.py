import requests
import json

grafana_url = "a5c07bf2eeabc479f99071aaddbac98b-364804466.ap-south-1.elb.amazonaws.com"
username = "admin"
password = "prom-operator"

base_url = "http://{}:{}@{}".format(username, password, grafana_url)

headers = {
    'Authorization': 'Bearer eyJrIjoiN0xNM1V4UWpMUkVoZXRKaWh2bVJya3IzZGNqb0dvTGkiLCJuIjoiQWRtaW4iLCJpZCI6MX0=',
    'Content-Type': 'application/json',
    'Accept': "application/json"
}

json_data = {
  "Name": "slack-alerts",  
  "Type":  "slack",
  "sendReminder": True,
  "frequency" : "15m",
  "settings": {
    "url" : "https://hooks.slack.com/services/9SUows",
    "Username":"devops1-bot",
    "recipient":"#monitoring",
    "Icon emoji":":smile:",
    "Icon Url":"https://avatars.githubusercontent.com/u/7195757",
    "token":"123"
  }
}

#for iconurl just search https://github.com/grafana.png
# {
#   "uid": "new-alert-notification", // optional
#   "name": "new alert notification",  //Required
#   "type":  "email", //Required
#   "isDefault": false,
#   "sendReminder": false,
#   "settings": {
#     "addresses": "dev@grafana.com"
#   }
# }


resp = requests.post(base_url + "/api/v1/provisioning/contact-points",headers=headers, json=json_data, verify=False)
# resp = requests.post(base_url + "/api/alert-notifications",headers=headers, json=json_data, verify=False) this is for legacy
print(json.dumps(resp.json(), indent=4))

