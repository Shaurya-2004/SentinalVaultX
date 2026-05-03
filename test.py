"""
Force reload .env and test credentials
Save as: force_reload_test.py
"""

import os
import sys

# Clear any cached environment variables
for key in list(os.environ.keys()):
    if key.startswith('TWILIO_') or key.startswith('EMAIL_') or key.startswith('SMTP_'):
        del os.environ[key]

# Force reload .env
from dotenv import load_dotenv
load_dotenv(override=True)  # override=True forces reload

import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client

print("="*60)
print("FORCE RELOADING .env FILE")
print("="*60)

# Check current directory
print(f"\nCurrent directory: {os.getcwd()}")
print(f".env file exists: {os.path.exists('.env')}")

if os.path.exists('.env'):
    print("\nReading .env file directly:")
    with open('.env', 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key = line.split('=')[0]
                if 'PASSWORD' in key or 'TOKEN' in key:
                    print(f"  {key}=***HIDDEN***")
                else:
                    print(f"  {line}")

print("\n" + "="*60)
print("CHECKING LOADED ENVIRONMENT VARIABLES")
print("="*60)

twilio_sid = os.getenv("TWILIO_ACCOUNT_SID")
twilio_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone = os.getenv("TWILIO_PHONE_NUMBER")
email_sender = os.getenv("EMAIL_SENDER")
email_password = os.getenv("EMAIL_PASSWORD")

print(f"TWILIO_ACCOUNT_SID: {twilio_sid[:10]}... (✓ SET)" if twilio_sid else "TWILIO_ACCOUNT_SID: ✗ MISSING")
print(f"TWILIO_AUTH_TOKEN: {'✓ SET' if twilio_token else '✗ MISSING'}")
print(f"TWILIO_PHONE_NUMBER: {twilio_phone}")
print(f"EMAIL_SENDER: {email_sender}")
print(f"EMAIL_PASSWORD: {'✓ SET (' + str(len(email_password)) + ' chars)' if email_password else '✗ MISSING'}")

print("\n" + "="*60)
print("TESTING EMAIL")
print("="*60)

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    print(f"Attempting login with {email_sender}...")
    server.login(email_sender, email_password)
    print("✓ EMAIL LOGIN SUCCESSFUL!")
    
    # Send test email
    msg = MIMEText("Test from ATM Security - Config Fixed!")
    msg["Subject"] = "✓ Email Working!"
    msg["From"] = email_sender
    msg["To"] = email_sender
    server.sendmail(email_sender, email_sender, msg.as_string())
    server.quit()
    print(f"✓ Test email sent to {email_sender}")
    
except Exception as e:
    print(f"✗ Email failed: {e}")

print("\n" + "="*60)
print("TESTING SMS")
print("="*60)

try:
    client = Client(twilio_sid, twilio_token)
    
    # Get actual phone numbers
    numbers = client.incoming_phone_numbers.list(limit=1)
    if numbers:
        actual_number = numbers[0].phone_number
        print(f"✓ Your Twilio number: {actual_number}")
        
        if twilio_phone == actual_number:
            print("✓ Phone number matches!")
            
            # Send test SMS
            print(f"Sending test SMS to +917081239249...")
            message = client.messages.create(
                body="✓ ATM Security SMS Working!",
                from_=twilio_phone,
                to="+919540991600"
            )
            print(f"✓ SMS SENT! SID: {message.sid}")
        else:
            print(f"✗ Number mismatch!")
            print(f"  .env has: {twilio_phone}")
            print(f"  Should be: {actual_number}")
    else:
        print("✗ No Twilio numbers found")
        
except Exception as e:
    print(f"✗ SMS failed: {e}")

print("\n" + "="*60)
print("DONE!")
print("="*60)