from mcp.server.fastmcp import FastMCP  
import resend  
import httpx
from dotenv import load_dotenv
import os
import resend 

PORT = os.environ.get("PORT", 10000)
mcp = FastMCP("Resend Email Server", host="0.0.0.0", port=PORT) 

@mcp.tool()   
def send_email(subject: str, to: str, from_email: str, content: str) -> str:  
    """Sends an email using the Resend API."""  
    try:   
        resend.api_key =os.getenv("RESEND_API")  
          
        params = {  
            "from": from_email,  
            "to": [to],  
            "subject": subject,  
            "html": content,  
        }  
        email = resend.Emails.send(params)  
        return f"Email sent successfully"  
    except ImportError as e:  
        return f"Import error: {e}. Make sure 'resend' package is installed."  
    except Exception as e:  
        return f"Email sending failed: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
