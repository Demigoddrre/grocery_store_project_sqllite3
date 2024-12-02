import requests

def get_power_bi_token(client_id, client_secret, tenant_id):
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
    payload = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'https://analysis.windows.net/powerbi/api/.default'
    }
    response = requests.post(url, data=payload)
    response.raise_for_status()
    return response.json().get("access_token")

def update_dataset(access_token, group_id, dataset_id, file_path):
    url = f"https://api.powerbi.com/v1.0/myorg/groups/{group_id}/datasets/{dataset_id}/tables/TableName/rows"
    headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}
    with open(file_path, 'r') as file:
        data = file.read()

    response = requests.put(url, headers=headers, data=data)
    response.raise_for_status()
    return response.json()

def get_embed_url(access_token, group_id, report_id):
    url = f"https://api.powerbi.com/v1.0/myorg/groups/{group_id}/reports/{report_id}"
    headers = {'Authorization': f'Bearer {access_token}'}

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json().get("embedUrl")
