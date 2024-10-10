from django.contrib import admin
from .models import (
    User, Student, Teacher, Course, Lesson, Assignment, Submission,
    Enrollment, CourseReview, Announcement, Progress, Notification, Exam
)

# Configuration pour le modèle User
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
#     search_fields = ('username', 'email', 'first_name', 'last_name')
#     list_filter = ('is_staff', 'is_active')

# Configuration pour le modèle Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'birthdate', 'niveau')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('niveau',)

# Configuration pour le modèle Teacher
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'expertise', 'experience_years')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'expertise')
    list_filter = ('expertise', 'experience_years')

# Configuration pour le modèle Course
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date', 'created_by')
    search_fields = ('name', 'description')
    list_filter = ('start_date', 'end_date')
    filter_horizontal = ('prerequisites',)
    
# Configuration pour le modèle Lesson
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'teacher', 'date_published', 'version')
    search_fields = ('title', 'course__name', 'teacher__username')
    list_filter = ('course', 'teacher', 'date_published')

# Configuration pour le modèle Assignment
@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'due_date', 'max_score', 'is_late')
    search_fields = ('title', 'lesson__title')
    list_filter = ('due_date', 'is_late')

# Configuration pour le modèle Submission
@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'student', 'grade', 'submitted_at', 'attempt_number')
    search_fields = ('assignment__title', 'student__username')
    list_filter = ('submitted_at',)
    readonly_fields = ('submitted_at',)

# Configuration pour le modèle Enrollment
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date', 'completed')
    search_fields = ('student__username', 'course__name')
    list_filter = ('completed', 'enrollment_date')

# Configuration pour le modèle CourseReview
@admin.register(CourseReview)
class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'rating', 'created_at')
    search_fields = ('course__name', 'student__username')
    list_filter = ('rating', 'created_at')

# Configuration pour le modèle Announcement
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('course', 'content', 'date_posted')
    search_fields = ('course__name', 'content')
    list_filter = ('date_posted',)

# Configuration pour le modèle Progress
@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('student', 'lesson', 'completed')
    search_fields = ('student__username', 'lesson__title')
    list_filter = ('completed',)

# Configuration pour le modèle Notification
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'created_at')
    search_fields = ('user__username', 'message')
    list_filter = ('is_read', 'created_at')

# Configuration pour le modèle Exam
@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'max_score', 'date')
    search_fields = ('course__name', 'title')
    list_filter = ('date',)
