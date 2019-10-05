#https://hooks.slack.com/services/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

import json
import urllib3
urllib3.disable_warnings()
http = http = urllib3.PoolManager()
def post_to_slack(message):
    slack_url = "https://hooks.slack.com/services/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"
    
    encoded_data = json.dumps({'text': message, 'username': "SQL Server", "icon_url": "https://d2.alternativeto.net/dist/icons/sql-server-management-studio_60533.png?width=200&height=200&mode=crop&upscale=false" }).encode('latin-1')
    response = http.request("POST", slack_url, body=encoded_data, headers={'Content-Type': 'application/json'})
    #print(str(response.status) + str(response.data))
#post_to_slack(message_txt_in)
post_to_slack('Mensagem Teste 3')

