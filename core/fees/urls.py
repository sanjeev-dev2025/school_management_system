from django.urls import path
from fees.views import (
    FeeStructureListCreateAPIView,
    FeeStructureRetrieveUpdateDestroyAPIView,
    StudentFeeListCreateAPIView,
    StudentFeeRetrieveAPIView
)

urlpatterns = [
    path(
        "structures/",
        FeeStructureListCreateAPIView.as_view(),
        name="fee-structure-list-create"
    ),

    path(
        "structures/<int:id>/",
        FeeStructureRetrieveUpdateDestroyAPIView.as_view(),
        name="fee-structure-detail"
    ),

    path(
        "student-fees/",
        StudentFeeListCreateAPIView.as_view(),
        name="student-fee-list-create"
    ),

    path(
        "student-fees/<int:id>/",
        StudentFeeRetrieveAPIView.as_view(),
        name="student-fee-detail"
    ),
]