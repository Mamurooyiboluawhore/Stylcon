from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags


def send_plain_text_email(subject, to_email, message, **kwargs):
    """Send a plain text email."""
    email = EmailMultiAlternatives(
        subject=subject,
        body=message,
        from_email="mamurooyibo@gmail.com",
        to=[to_email],  # Recipient's email address(es)
    )

    email.send()