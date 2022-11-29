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

# json_data =  {
#   "type":  "email",
#   "settings": {
#     "addresses": "vaibhav.kumar@knoldus.com"
#   }
# }


json_data = {  
  "type":  "slack",
  "settings": {
    "url" : "https://hooks.slack.com/services/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",
    "Username":"devops1-bot",
    "token" : "123"
  }
}



resp = requests.post(base_url + "/api/alert-notifications/test",headers=headers, json=json_data, verify=False)
print(json.dumps(resp.json(), indent=4))

