import base64
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import make_msgid

def send_message(to,message):
    """Send an email message.
    Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.
    Returns:
    Sent Message.
    """
    try:
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login('celerymailtest@gmail.com', 'avnlihsgbwvdaazh')
        text = message.as_string()
        session.sendmail('celerymailtest@gmail.com', to, text)
        session.quit()
        # message = (service.users().messages().send(userId=user_id, body=message)
        #            .execute())
        # print('Message Id: %s' % message['id'])
        return message
    except Exception as error:
        print('An error occurred: %s' % error)


def create_message(sender, to, subject, message_text):
    """Create a message for an email.
    Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.
    Returns:
    An object containing a base64url encoded email object.
    """
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = ' '.join(to)
    message['Subject'] = subject
    message["Message-ID"] = make_msgid()
    message.attach(MIMEText(message_text))
    return message

    # message = MIMEText(message_text, "html")
    # message['to'] = to
    # message['from'] = sender
    # message['subject'] = subject
    # b64_bytes = base64.urlsafe_b64encode(message.as_bytes())
    # b64_string = b64_bytes.decode()
    # return {'raw': b64_string}
