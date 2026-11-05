
from django.db import models


class FeeStructure(models.Model):

    class FeeType(models.TextChoices):
        ADMISSION = "ADMISSION", "admission"
        TUITION = "TUITION", "tuition"
        EXAM = "EXAM", "exam"
        LIBRARY = "LIBRARY", "library"
        OTHER = "OTHER", "other"

    name = models.CharField(max_length=20)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    fee_type = models.CharField(
        max_length=20,
        choices=FeeType.choices
    )

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class StudentFee(models.Model):

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        PARTIAL="PARTIAL","partial"
        PAID = "PAID", "Paid"

    student = models.ForeignKey(
        "students.StudentProfile",
        on_delete=models.PROTECT,
        related_name="student_fees"
    )

    fee_structures = models.ManyToManyField(
        FeeStructure,
        related_name="student_fees"
    )

    academic_year = models.CharField(max_length=20)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    due_date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.amount}"
