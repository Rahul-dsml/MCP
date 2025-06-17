import requests
from auth import get_token

GRAPH_API = "https://graph.microsoft.com/v1.0"

def get_headers():
    token = get_token()
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

def read_latest_emails(count=5):
    url = f"{GRAPH_API}/me/mailFolders/Inbox/messages?$top={count}&$select=subject,receivedDateTime,from"
    res = requests.get(url, headers=get_headers())
    res.raise_for_status()
    return res.json().get("value", [])

def search_emails(query):
    url = f"{GRAPH_API}/me/messages?$search=\"{query}\""
    res = requests.get(url, headers=get_headers())
    res.raise_for_status()
    return res.json().get("value", [])

def read_email_body(message_id):
    url = f"{GRAPH_API}/me/messages/{message_id}"
    res = requests.get(url, headers=get_headers())
    res.raise_for_status()
    return res.json().get("body", {}).get("content", "No content.")

def send_email(to_email, subject, content):
    url = f"{GRAPH_API}/me/sendMail"
    payload = {
        "message": {
            "subject": subject,
            "body": {
                "contentType": "HTML",
                "content": content
            },
            "toRecipients": [
                {
                    "emailAddress": {
                        "address": to_email
                    }
                }
            ]
        }
    }
    res = requests.post(url, headers=get_headers(), json=payload)
    res.raise_for_status()
    return {"status": "Email sent"}
