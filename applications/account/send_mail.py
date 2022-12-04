from django.core.mail import send_mail

def send_activate_email(email, code):
    full_link = f'http://localhost:8000/account/{code}'
    send_mail(
        'User activation',
        full_link,
        'rafievvvv@gmail.com',
        [email]
    )