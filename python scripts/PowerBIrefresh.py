import adal
import requests
import json
import pandas

authority_url = 'https://login.windows.net/common'
resource_url = 'https://analysis.windows.net/powerbi/api'
client_id = 'cebd27f5-a9ef-47ed-a6f6-84a21c14eef6'
username = 'joao@jmmjholdings.onmicrosoft.com'
password = 'Aligator123@'

context = adal.AuthenticationContext(authority=authority_url,
                                     validate_authority=True,
                                     api_version=None)
token = context.acquire_token_with_username_password(resource=resource_url,
                                                     client_id=client_id,
                                                     username=username,
                                                     password=password)
access_token = token.get('accessToken')
groups_request_url = 'https://api.powerbi.com/v1.0/myorg/groups'
header = {'Authorization': f'Bearer {access_token}'}
groups_request = json.loads(requests.get(url=groups_request_url, headers=header).content)
groups = [d['id'] for d in groups_request['value']]
for group in groups:
    datasets_request_url = 'https://api.powerbi.com/v1.0/myorg/groups/' + group + '/datasets'
    datasets_request = json.loads(requests.get(url=datasets_request_url, headers=header).content)
    datasets = [d['id'] for d in datasets_request['value']]
    for dataset in datasets:
        refresh_url = 'https://api.powerbi.com/v1.0/myorg/groups/' + group + '/datasets/' + dataset + '/refreshes'
        r = requests.post(url=refresh_url, headers=header)
final = pandas.DataFrame()