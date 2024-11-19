from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment
import base64
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def send_email_with_attachment():
    """Sends an email with an optional attachment."""
    try:
        # Collect input from the user
        print("\n=== Send Email ===")
        recipient = input("Enter recipient email address: ")
        subject = input("Enter email subject: ")
        body = input("Enter email body: ")
        attachment_path = input("Enter the path to the attachment (leave blank if none): ")

        # Create the email
        message = Mail(
            from_email=os.getenv('SENDER_EMAIL'),  # Set your verified sender email in the .env file
            to_emails=recipient,
            subject=subject,
            plain_text_content=body,
        )

        # Add attachment if a valid path is provided
        if attachment_path and os.path.exists(attachment_path):
            with open(attachment_path, 'rb') as f:
                file_data = f.read()
                encoded_file = base64.b64encode(file_data).decode()  # Encode the file
                attachment = Attachment(
                    file_content=encoded_file,
                    file_type="application/octet-stream",
                    file_name=os.path.basename(attachment_path),
                    disposition="attachment"
                )
                message.attachment = attachment
                print(f"Attachment {os.path.basename(attachment_path)} added.")
        elif attachment_path:
            print("Invalid file path. Email will be sent without attachment.")

        # Send the email via SendGrid
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(f"Email sent successfully to {recipient}! Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred while sending the email: {e}")
