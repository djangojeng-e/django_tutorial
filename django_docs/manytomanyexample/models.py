from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=50)
    enrolments = models.ManyToManyField(Student, through='Enrolment')

    def __str__(self):
        return self.name


class Enrolment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_date = models.DateTimeField()
    finished_date = models.DateTimeField(null=True)

    AcademicType = models.TextChoices('AcademicType', 'A B C D E F')

    academic_record = models.CharField(null=True, choices=AcademicType.choices, max_length=10)

    def __str__(self):
        return self.student, self.course, self.enrolled_date, self.finished_date, self.academic_record



