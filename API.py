import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Token abc'
}

r = requests.post('https://url/4/api/call', headers = headers)

print(r.json())