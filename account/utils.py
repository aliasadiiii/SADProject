from django.core.mail import send_mail


def send_activation_email(to, activation_link):
    body = """
    Your activation link:
    {}
    """.format(activation_link)

    send_mail('Activation Link', body, '', [to], fail_silently=False)


def send_forget_password_email(to, forget_password_link):
    body = """
    Your forget-password link:
    {}
    """.format(forget_password_link)

    send_mail('Forget-password Link', body, '', [to], fail_silently=False)
