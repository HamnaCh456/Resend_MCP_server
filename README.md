# Resend Email MCP Server

A tiny, zero-config MCP (Model-Context-Protocol) server that lets LLMs send email through [Resend](https://resend.com).  
Plug it into Claude Desktop, Cursor, or any other MCP client and start sending messages in seconds.

---
## Demo
[Watch the Demo](https://youtu.be/t3ALuFP2JaY)

---
## Deployed MCP Server Link
[link](https://smithery.ai/server/@HamnaCh456/resend_mcp_server345)

---
## Quick start

1. **Grab the code**
   ```bash
   git clone https://github.com/HamnaCh456/Resend_MCP_server.git
   cd resend-email-mcp
   ```

2. **Install deps**
   ```bash
   pip install -r requirements.txt        # or: uv pip install fastmcp resend python-dotenv httpx
   ```

3. **Set your Resend API key**
   ```bash
   export RESEND_API=re_YOUR_RESEND_KE
   ```

4. **Run the server**
   ```bash
   After configuring the settings.json(in case you are using Gemini CLI) file ,give command to LLM to send an email with other specifications.
   ```
---

## ⚙️ Environment variables

| Variable     | Default | Purpose                                  |
|--------------|---------|------------------------------------------|
| `RESEND_API` | —       | **Required** Resend API key               |
| `PORT`       | 10000   | Port to bind when running in HTTP mode   |

---

## 🔧 Exposed tool

### `send_email`

Send a single HTML email.

```json
{
  "subject": "Hello from MCP",
  "to": "friend@example.com",
  "from_email": "you@yourdomain.com",
  "content": "<h1>Hi!</h1><p>Sent by an LLM 🤖</p>"
}
```

Return value: `"Email sent successfully"` or an error message.

---

## 🧪 Example session in Claude Desktop

1. Claude: *“Send an email to alice@example.com with subject ‘Meeting notes’ and the notes in the chat.”*
2. You type: `@send_email`  
   Claude fills the parameters and calls the tool.  
3. Email is delivered—no copy-paste needed.

---

## Requirements

- Python 3.9+
- `fastmcp`, `resend`, `python-dotenv`, `httpx`

Install them quickly with:

```bash
pip install fastmcp resend python-dotenv httpx
```
---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| “Import error: resend” | `pip install resend` |
| “401 Unauthorized” | Check `RESEND_API` key and domain verification in Resend dashboard |
| Port already in use | `export PORT=10001` or any free port |

---

Happy emailing!
