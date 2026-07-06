def send_email(to: str, subject: str, body: str):
    # SECURITY: do not log full email content in production
    import sys
    msg = f"[EMAIL] To: {to} | Subject: {subject}"
    try:
        print(msg)
    except UnicodeEncodeError:
        print(msg.encode(sys.stdout.encoding or 'ascii', errors='replace').decode(sys.stdout.encoding or 'ascii'))
    # In real MCP, this would call an email API


