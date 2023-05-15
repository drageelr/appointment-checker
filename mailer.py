import yagmail

EMAIL='automater.pro99@gmail.com'
PASS='fczuwdeqqpaujqra'

def send_mail(subject, contents):
    yag = yagmail.SMTP(EMAIL, PASS)
    yag.send(
        to='hammadn99@gmail.com',
        subject=subject,
        contents=contents,
    )

if __name__ == '__main__':
    send_mail('hammadn99@gmail.com', 'Test Email', 'Test Content')