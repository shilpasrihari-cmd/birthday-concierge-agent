def send_email(to: str, subject: str, body: str):
    # SECURITY: do not log full email content in production
    print(f"[EMAIL] To: {to} | Subject: {subject}")
    # In real MCP, this would call an email API

