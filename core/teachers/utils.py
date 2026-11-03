from django.core.mail import send_mail
from django.conf import settings


def send_teacher_credentials(teacher, password):

    subject = "Your College teacher Account"

    message = f"""
Hello {teacher.first_name},

Your teacher account has been successfully created.
username:{teacher.user.username}
teacher ID: {teacher.teacher_id}
Email: {teacher.user.email}
Temporary Password: {password}

Please log in using these credentials and change
your password immediately.

Regards,
College Administration
"""

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [teacher.user.email],
        fail_silently=False,
    )