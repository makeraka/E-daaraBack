from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# ************************ classe abstraite des utilisateur ***************
class User(AbstractUser):
    # Ajoute d'autres champs ici
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Change le nom ici
        blank=True,
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Change le nom ici
        blank=True,
    )

# ********************** la classe des cours *********************************************
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    prerequisites = models.ManyToManyField('self', symmetrical=False, blank=True)
    created_by = models.ForeignKey('User', on_delete=models.CASCADE)  # Utilisateur qui a créé le cours

    def __str__(self):
        return self.name

# ******************** class pour etudiant *********************
class Student(User):
    birthdate = models.DateField(null=True, blank=True)
    enrolled_courses = models.ManyToManyField(Course, blank=True, related_name='students_enrolled')
    niveau = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return f"Student: {self.username}"  # Ajoute 'Student:' pour une distinction claire
    
# ********************** class pour professeurs *********************************
class Teacher(User):
    expertise = models.CharField(max_length=255)
    experience_years = models.PositiveIntegerField(null=True, blank=True)
    courses = models.ManyToManyField(Course, related_name='teachers', blank=True)
    
    def __str__(self):
        return f"Teacher: {self.username}"  # Ajoute 'Teacher:' pour une distinction claire

# ****************************** class pour Lesson *****************************
class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, related_name='lessons_taught', on_delete=models.CASCADE)
    date_published = models.DateField(auto_now_add=True)
    media_file = models.FileField(upload_to='lessons/media/', null=True, blank=True)
    version = models.PositiveIntegerField(default=1) # permet d'avoir une nouvel version des lessons afin de modifier le contenu au fil du temps 


    def __str__(self):
        return self.title

# ************************************* class pour des Devoir) ****************************
class Assignment(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='assignments', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    max_score = models.IntegerField()
    is_late = models.BooleanField(default=False)

    def __str__(self):
        return f"Devoir: {self.title}" 

# ****************************** class pour Submission de devoirs **********************
class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, related_name='submissions', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='submissions', on_delete=models.CASCADE)
    submission_file = models.FileField(upload_to='submissions/', null=True, blank=True)
    grade = models.IntegerField(null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    attempt_number = models.PositiveIntegerField(default=1)  #garde l'historique des submissions

    def __str__(self):
        return f'{self.assignment.title} - {self.student.username}'
    

# ****************************** class pour Enrollment (inscription )********************************

class Enrollment(models.Model):
    student = models.ForeignKey(Student, related_name='enrollments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.student.username} enrolled in {self.course.name}'

# *******************************class pour  CourseReview(pour l'evaluation des cours par les etudiants*************************

class CourseReview(models.Model):
    course = models.ForeignKey(Course, related_name='reviews', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='course_reviews', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(1, '1 étoile'), (2, '2 étoiles'), (3, '3 étoiles'), (4, '4 étoiles'), (5, '5 étoiles')])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
# ************************ class pour Announcement Interaction et Communication ******************
class Announcement(models.Model):
    course = models.ForeignKey(Course, related_name='announcements', on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

# ***************************class pour le progression **********************
class Progress(models.Model):
    student = models.ForeignKey(Student, related_name='progress', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name='progress', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    

# système de notifications pour alerter les étudiants des nouvelles annonces, des devoirs à rendre, ou des évaluations.
class Notification(models.Model):
    user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    

# classe pour  les tests ou les examens
class Exam(models.Model):
    course = models.ForeignKey(Course, related_name='exams', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    max_score = models.IntegerField()
    date = models.DateField()


