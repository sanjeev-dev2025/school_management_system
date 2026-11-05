
from rest_framework import serializers
from django.db import transaction

from fees.models import FeeStructure, StudentFee


class FeeStructureSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeeStructure
        fields = "__all__"
        read_only_fields = ["id", "created_at"]


class StudentFeeSerializer(serializers.ModelSerializer):

    fee_structures = serializers.PrimaryKeyRelatedField(
        queryset=FeeStructure.objects.all(),
        many=True
    )

    class Meta:
        model = StudentFee
        fields = "__all__"
        read_only_fields = [
            "id",
            "created_at",
            "amount",
            "status"
        ]

    def validate(self, attrs):
        print("RECEIVED FEE STRUCTURES:", attrs.get("fee_structures"))
        return attrs

    @transaction.atomic
    def create(self, validated_data):
        fee_structures = validated_data.pop("fee_structures")

        total_amount = sum(
            fee.amount for fee in fee_structures
        )

        student_fee = StudentFee.objects.create(
            amount=total_amount,
            **validated_data
        )

        student_fee.fee_structures.set(fee_structures)

        return student_fee