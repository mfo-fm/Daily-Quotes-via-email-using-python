# Daily-Quotes-via-email-using-python

The Python script sends daily emails containing randomly selected quotes from a CSV file. It reads quotes from the CSV file, selects a random quote, constructs an email message with the quote, author, and tags, and sends the email using SMTP with SSL encryption. The script is scheduled to run daily to automate the process of sending inspirational quotes via email.

The task scheduler is configured to execute the Python script daily at a specified time, automating the process of sending daily quotes via email, I used Windows for this by creating a task and editing appropriate fields.

I can also use my command prompt, by entering the file path, then I use the schtasks command to schedule a task to run your Python script at a specific time like this schtasks /create /tn "DailyEmail" /tr "C:\Users\******\AppData\Local\Programs\Python\python.exe C:\Users\*****\****\***\****\daily_email_quotes.py" /sc daily /st 08:00
