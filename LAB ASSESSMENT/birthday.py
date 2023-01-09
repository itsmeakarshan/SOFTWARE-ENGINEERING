import datetime
import smtplib

# Set your email credentials
EMAIL_ADDRESS = "akarshanrasyal4@gmail.com"
EMAIL_PASSWORD = "zsmntpssemqmqcwc"

# Connect to the email server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login('akarshanrasyal4@gmail.com','zsmntpssemqmqcwc')

def send_email(recipient_email, subject, body):
    """Sends an email to the specified recipient."""
    server.sendmail(EMAIL_ADDRESS, recipient_email, f"Subject: {subject}\n\n{body}")

def send_birthday_greetings(user_id, users_data):
    """Sends birthday greetings to the specified user via email."""
    # Fetch the user's birthday and email address from the users_data dictionary
    birthday = users_data[user_id]["birthday"]
    email = users_data[user_id]["email"]

    # Check if today is the user's birthday
    today = datetime.datetime.now()
    if (today.month, today.day) == (birthday.month, birthday.day):
        # Send birthday greetings via email
        subject = "Happy Birthday!"
        body = f"Happy birthday, {users_data[user_id]['name']}!\n\nWishing you a fantastic day and a great year ahead."
        send_email(email, subject, body)

# Example data for two users
users_data = {
    "user1": {
        "name": "AKarsshan",
        "birthday": datetime.datetime(2023, 1, 9),
        "email": "akarshanrasyal@gmail.com",
    },
    "user2": {
        "name": "Akarshan",
        "birthday": datetime.datetime(2023, 1, 9),
        "email": "udsakarshan174@gmail.com",
    },
}

# Send birthday greetings to all users
for user_id in users_data:
    send_birthday_greetings(user_id, users_data)

# Disconnect from the email server
server.quit()