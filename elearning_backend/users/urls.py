from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AssignmentViewSet,
    EnrollmentViewSet,
    LessonViewSet,
    StudentViewSet,
    SubmissionViewSet,
    TeacherViewSet,
    CourseViewSet
)

# Enregistrement des viewsets avec le routeur par défaut
router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'submissions', SubmissionViewSet)
router.register(r'enrollments', EnrollmentViewSet)

# URL patterns
urlpatterns = [
     path('api/v1/', include(router.urls)), # Inclut toutes les routes du routeur
]
