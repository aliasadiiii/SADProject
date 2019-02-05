from django.core.mail import send_mail

from .models import Purchase


def send_purchase_state_change_email(purchase):
    body = "Your purchase state has been changed to {}".format(
        dict(Purchase.STATE_CHOICES)[purchase.state])

    send_mail('Purchase #{}'.format(purchase.reference_token), body, '',
              [purchase.user.email], fail_silently=False)
