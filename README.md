# 📬 MCP SERVER with Microsoft Graph (OUTLOOK)

This project exposes a REST API using **FastAPI** to interact with **Microsoft Outlook/M365 email** accounts via **Microsoft Graph API**. It supports operations like reading, searching, and sending emails after authenticating using **device code flow**.

---

## 🚀 Features

- ✅ Authenticate with Microsoft account (device code)
- 📥 Fetch latest emails
- 🔍 Search emails by query (subject/body)
- 📖 Read full body of a specific email
- ✉️ Send emails using Graph API

---

## 🧪 Example Usage

| Endpoint | Description |
|----------|-------------|
| `GET /emails?count=3` | Get the latest 3 emails |
| `GET /search?query=invoice` | Search for emails with the word "invoice" |
| `GET /emails/{message_id}` | Fetch the full body of a specific email |
| `POST /send` | Send an email (see JSON format below) |

### Example JSON for Sending Email
```json
{
  "to": ["recipient@example.com"],
  "subject": "Test Email",
  "body": "This is a test email sent from FastAPI."
}
````

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Rahul-dsml/MCP.git
cd MCP/email_testing
```

### 2. Create `.env` File

```env
client_id=YOUR_CLIENT_ID_HERE
tenant_id=common
```

> Ensure that your registered Azure AD app has the following **delegated API permissions**:
>
> * `Mail.Read`
> * `Mail.Send`
> * `User.Read`

### 3. Create a Virtual Environment & Install Dependencies

```bash
conda create -n emailenv python=3.10
conda activate emailenv
pip install -r requirements.txt
```

### 4. Run the Server

```bash
uvicorn email_api:app --reload
```

Then open your browser or use `curl` to access:

```http
http://localhost:8000/docs
```

> 🔐 First time access will ask you to visit `https://microsoft.com/devicelogin` and enter a code.

---

## 🧰 Tech Stack

* Python 3.10
* FastAPI
* Microsoft Authentication Library (MSAL)
* Microsoft Graph API
* Requests
* Dotenv

---

## 🧑 Author

**Rahul Singh**
GitHub: [@Rahul-dsml](https://github.com/Rahul-dsml)


