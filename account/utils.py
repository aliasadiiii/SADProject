from django.core.mail import send_mail


def send_activation_email(to, activation_link):
    body = """
    Your activation link:
    {}
    """.format(activation_link)

    send_mail('Activation Link', body, '', [to], fail_silently=False)
