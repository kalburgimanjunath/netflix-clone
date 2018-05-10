from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_welcome_email(name,receiver):
    subject='Welcome to The better Netflix all you need is warmth.'
    sender = 'mutwirimochiemo@gmail.com'

    text_content = render_to_string('email/netflix.txt', {"name":name})
    html_context = render_to_string('email/netflix.html',{"name":name})
    msg = EmailMultiAlternatives(subject, text_content, sender,[receiver])
    msg.attach_alternatve(html_context,'text.html')
    msg.send()
