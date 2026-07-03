from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=100, default="Computer Science")
    year = models.IntegerField(default=1)
    semester = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.roll_no}"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    credits = models.IntegerField(default=3)
    semester = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Marks(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    internal_marks = models.IntegerField(default=0)
    external_marks = models.IntegerField(default=0)

    @property
    def total_marks(self):
        return self.internal_marks + self.external_marks

    @property
    def grade(self):
        total = self.total_marks
        if total >= 91: return "O"
        elif total >= 81: return "A+"
        elif total >= 71: return "A"
        elif total >= 61: return "B+"
        elif total >= 51: return "B"
        elif total >= 45: return "C"
        else: return "U"

    @property
    def grade_point(self):
        total = self.total_marks
        if total >= 91: return 10
        elif total >= 81: return 9
        elif total >= 71: return 8
        elif total >= 61: return 7
        elif total >= 51: return 6
        elif total >= 45: return 5
        else: return 0

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.total_marks}"
