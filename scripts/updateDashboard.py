import sys
import requests
import json
import csv

widgets = "http://cam-dev03.production-mr.indix.tv:3030/widgets/"
events = "http://cam-dev03.production-mr.indix.tv:3030/dashboards/*"
authToken = "YOUR_AUTH_TOKEN"

with open(sys.argv[1]) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dataUpdate = { "auth_token": authToken, "current": row["current"], "last": row["last"] }
        requests.post(widgets + row["kpi"], data=json.dumps(dataUpdate))
    refreshEvent = { "auth_token": authToken, "event": "reload"}
    requests.post(events + "*", data=json.dumps(refreshEvent))
