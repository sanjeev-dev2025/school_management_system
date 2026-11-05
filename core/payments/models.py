
from django.db import models


class Payment(models.Model):

    student_fee = models.ForeignKey(
        "fees.StudentFee",
        on_delete=models.PROTECT,
        related_name="payments"
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_date = models.DateTimeField(auto_now_add=True)

    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student_fee.student} - Rs. {self.amount}"
