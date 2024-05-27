import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import pandas as pd
import random

def send_email():
    # Email account credentials
    from_email = "olaniyanfarouqmo@gmail.com"
    password = "glhl fgaz pqwf cuyg"  # Use the generated app password
    to_email = "olaniyanfarouqmo@yahoo.com"

    # Load quotes from CSV file
    csv_path = r'C:\Users\bluechip\Desktop\TUTORIALS\PROJECTS\quotes.csv'  # Replace with the path to your CSV file
    quotes_df = pd.read_csv(csv_path)

    # Select a random quote
    random_quote = quotes_df.sample(1).iloc[0]
    quote = random_quote['Quote']
    author = random_quote['Author']
    tags = random_quote['Tags']

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "Daily Quote - " + datetime.datetime.now().strftime("%Y-%m-%d")

    # Email body with quote, author, and tags
    body = f"\"{quote}\"\n\n- {author}\n\nTags: {tags}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Create server object with SSL option
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(from_email, password)

        # Send email
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print(f"Email sent successfully to {to_email}.")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

if __name__ == "__main__":
    send_email()
