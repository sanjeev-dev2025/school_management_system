from django.core.mail import send_mail
from django.conf import settings


def send_student_credentials(student, password):

    subject = "Your College Student Account"

    message = f"""
Hello {student.first_name},

Your student account has been successfully created.
username:{student.user.username}
Student ID: {student.student_id}
Email: {student.user.email}
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
        [student.user.email],
        fail_silently=False,
    )