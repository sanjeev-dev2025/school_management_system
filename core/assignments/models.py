from django.db import models
from teachers.models import TeacherProfile
from students.models import StudentProfile
from cloudinary_storage.storage import RawMediaCloudinaryStorage


class Assignment(models.Model):

    teacher = models.ForeignKey(
        TeacherProfile,
        on_delete=models.PROTECT,
        related_name="assignments"
    )

    title = models.CharField(max_length=150)
    description = models.TextField()

    grade = models.CharField(
        max_length=2,
        choices=StudentProfile.Grade.choices
    )

    subject = models.CharField(max_length=100)
    questions=models.FileField(upload_to='assessment/questions',blank=True,null=True,storage=RawMediaCloudinaryStorage())

    deadline= models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - Grade {self.grade}"

class AssignmentSubmission(models.Model):

    assignment = models.ForeignKey(
        Assignment,
        on_delete=models.CASCADE,
        related_name="submissions"
    )

    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name="assignment_submissions"
    )

    

    submitted_answers=models.FileField(upload_to='assessment/submissions',blank=True,null=True,storage=RawMediaCloudinaryStorage())        

    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["assignment", "student"],
                name="unique_student_assignment_submission"
            )
        ]

    def __str__(self):
        return f"{self.student} - {self.assignment}"