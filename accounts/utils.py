from django.core.mail import send_mail
from .models import EmailOTP
from django.conf import settings


def send_otp_to_user(user, code=None, via_sms=False):
    if code is None:
        otp_obj = EmailOTP.create_for_user(user)

    else:
        expires_at = EmailOTP.expiry_time()
        otp_obj = EmailOTP.objects.create(user=user, code=code, expires_at=expires_at)
        return otp_obj
    
    from_email = getattr(settings, 'EMAIL_HOST_USER', settings.DEFAULT_FROM_EMAIL)
    send_mail(
        'Your OTP code ✔',
        f'Your verification code id {otp_obj.code}',
        from_email,
        [user.email],
        fail_silently=False,
    )
    return otp_obj
