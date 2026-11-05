from django.utils import timezone
from rest_framework import serializers
from assignments.models import Assignment, AssignmentSubmission


class AssignmentSerializer(serializers.ModelSerializer):

    teacher = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Assignment
        fields = "__all__"
        read_only_fields = ["id", "teacher", "created_at"]

    def validate_questions(self, file):
        if not file:
            return file

        allowed_extensions = [".pdf", ".jpg", ".jpeg", ".png"]
        allowed_types = [
            "application/pdf",
            "image/jpeg",
            "image/png"
        ]

        filename = file.name.lower()
        content_type = getattr(file, "content_type", None)

        if not any(filename.endswith(ext) for ext in allowed_extensions):
            raise serializers.ValidationError(
                "Only PDF, JPG, JPEG and PNG files are allowed."
            )

        if content_type not in allowed_types:
            raise serializers.ValidationError(
                "Invalid file type. Upload a PDF or image."
            )

        if file.size > 10 * 1024 * 1024:
            raise serializers.ValidationError(
                "File size cannot exceed 10 MB."
            )

        return file

class AssignmentSubmissionSerializer(serializers.ModelSerializer):

    student = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = AssignmentSubmission
        fields = "__all__"
        read_only_fields = ["id", "student", "submitted_at"]

    def validate_submission_file(self, file):
        if not file:
            return file

        allowed_extensions = [".pdf", ".jpg", ".jpeg", ".png"]
        allowed_types = [
            "application/pdf",
            "image/jpeg",
            "image/png"
        ]

        filename = file.name.lower()
        content_type = getattr(file, "content_type", None)

        if not any(filename.endswith(ext) for ext in allowed_extensions):
            raise serializers.ValidationError(
                "Only PDF, JPG, JPEG and PNG files are allowed."
            )

        if content_type not in allowed_types:
            raise serializers.ValidationError(
                "Invalid file type. Upload a PDF or image."
            )

        if file.size > 10 * 1024 * 1024:
            raise serializers.ValidationError(
                "File size cannot exceed 10 MB."
            )

        return file

    def validate(self, attrs):
        request = self.context.get("request")
        assignment = attrs.get(
            "assignment",
            getattr(self.instance, "assignment", None)
        )

        if request and assignment:
            student = request.user.student_profile

            if student.grade != assignment.grade:
                raise serializers.ValidationError(
                    "You cannot submit an assignment for another grade."
                )
            if timezone.now()>= assignment.deadline:
                raise serializers.ValidationError(
                    "assignment deadline is passed"
                )

        submission_file = attrs.get( 
            "submission_file",
            getattr(self.instance, "submission_file", None)
        )
    
        if  not submission_file:
            raise serializers.ValidationError(
                "Please upload a file."
            )

        return attrs