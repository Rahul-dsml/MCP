from fastapi import FastAPI, HTTPException
from models import EmailRequest
import graph_client

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Email API is running."}

@app.get("/emails")
def get_emails(count: int = 5):
    try:
        return graph_client.read_latest_emails(count)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/search")
def search_mails(query: str):
    try:
        return graph_client.search_emails(query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/emails/{message_id}")
def get_email_body(message_id: str):
    try:
        return {"body": graph_client.read_email_body(message_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/send")
def send_mail(request: EmailRequest):
    try:
        return graph_client.send_email(request.to_email, request.subject, request.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
