from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Assignment, Enrollment, Lesson, Student, Submission, Teacher, Course
from .serializers import (
    AssignmentSerializer,
    EnrollmentSerializer,
    LessonSerializer,
    StudentSerializer,
    SubmissionSerializer,
    TeacherSerializer,
    CourseSerializer
)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Logique pour créer un étudiant
        serializer.save()

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Logique pour créer un professeur
        serializer.save()

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Logique pour créer un cours (uniquement pour l'admin)
        serializer.save()

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Logique pour créer une leçon
        serializer.save()

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Logique pour créer un devoir
        serializer.save()

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Logique pour créer une soumission
        serializer.save()

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Logique pour inscrire un étudiant à un cours
        serializer.save()


from rest_framework.exceptions import PermissionDenied

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if not self.request.user.is_superuser:  # Vérifie si l'utilisateur est un admin
            raise PermissionDenied("Vous n'avez pas la permission de créer un cours.")
        serializer.save()
