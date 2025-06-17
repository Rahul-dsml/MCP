import os
from dotenv import load_dotenv
from msal import PublicClientApplication

load_dotenv()
CLIENT_ID = os.getenv("client_id")
AUTHORITY = f"https://login.microsoftonline.com/{os.getenv('tenant_id_common')}"
SCOPES = ["Mail.ReadWrite", "Mail.Send", "User.Read"]

app = PublicClientApplication(CLIENT_ID, authority=AUTHORITY)
access_token = None

def get_token():
    global access_token
    accounts = app.get_accounts()
    result = app.acquire_token_silent(SCOPES, account=accounts[0]) if accounts else None

    if not result:
        flow = app.initiate_device_flow(scopes=SCOPES)
        if "user_code" not in flow:
            raise Exception("Device flow initiation failed.")
        print("Go to:", flow["verification_uri"])
        print("Enter code:", flow["user_code"])
        result = app.acquire_token_by_device_flow(flow)
    
    access_token = result.get("access_token")
    return access_token
