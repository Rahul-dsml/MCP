from pydantic import BaseModel


class EmailRequest(BaseModel):
    to_email: str
    subject: str
    content: str
