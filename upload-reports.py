import requests

API_TOKEN = 'defectdojo_api_token'

headers = {
    'Authorization': API_TOKEN
}

url = 'https://demo.defectdojo.org/api/v2/import-scan/'

data = {
    'scan_type': 'Gitleaks Scan',
    'active': 'true',
    'verified': 'true',
    # 'minimum_severity': 'low',
    'engagement': '21',  # This is the engagement id
}

files = {
    'file': open('gitleaks-report.json', 'rb')
}

response = requests.post(url, headers=headers, files=files, data=data)
if response.status_code == 201:
    print('Scan report imported successfully')
else:
    print('Failed to import scan report')
    print(response.content)