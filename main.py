import requests
import json
import datetime

url = "https://discord.com/api/v9/auth/login"
headers = {
    "accept": "/",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "content-length": "125",
    "content-type": "application/json",
    "origin": "https://discord.com",
    "referer": "https://discord.com/login",
    "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "x-debug-options": "bugReporterEnabled",
    "x-discord-locale": "en-US",
    "x-discord-timezone": "Asia/Calcutta",
    "x-super-properties": 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiaGFzX2NsaWVudF9tb2RzIjpmYWxzZSwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTM0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjM3Njg0MCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
}
payload = {
    "gift_code_sku_id": None,
    "login": "YOUR EMAIL",
    "login_source": None,
    "password": "YOUR PASSWORD",
    "undelete": False,
}
response = requests.post(url, headers=headers, data=json.dumps(payload))

now = datetime.datetime.now()
timestamp = now.strftime("%H:%M:%S")

if response.status_code == 200:
    response_data = response.json()
    if 'token' in response_data:
        token = response_data['token']
        print(f"[{timestamp}] | [/] Fetched Token > {token}")
    else:
        print(f"[{timestamp}] | [/] Token not found in the response.")
else:
    print(f"[{timestamp}] | [/] Login failed with status code: {response.status_code}")
