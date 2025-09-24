import os
from typing import Dict

import sendgrid
from sendgrid.helpers.mail import Mail, Email, Content, To
from agents import Agent, function_tool


@function_tool
def send_email(body: str):
    """
    Send out emails with the given body to all sales prospects
    """
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("matt@matt-sikes.com")
    to_email = To("emsikes@gmail.com")
    content = Content("text/plain", body)
    mail = Mail(from_email, to_email, "Sales email", content).get()
    response = sg.client.mail.send.post(request_body=mail)
    return {"status": "success"}

INSTRUCTIONS = """You are able to send a nicely formatted html email based on a detailed report.
You will be provided with a detailed report.  You should use your tool to send one email, providing the \
report converted into a clean, well presented html with an appropriate subject line."""

email_agent = Agent(
    name="Email agent",
    instructions=INSTRUCTIONS,
    tools=[send_email],
    model="gpt-4o-mini",
)