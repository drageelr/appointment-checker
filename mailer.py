import os
import yagmail

EMAIL=os.environ.get('SENDER_EMAIL')
PASS=os.environ.get('SENDER_PASS')

def send_mail(subject, contents):
    yag = yagmail.SMTP(EMAIL, PASS)
    yag.send(
        to=os.environ.get('RECVR_EMAILS').split(' '),
        subject=subject,
        contents=contents,
    )

if __name__ == '__main__':
    send_mail('hassan.tanveer0097@gmail.com', 'Test Email', 'Test Content')
