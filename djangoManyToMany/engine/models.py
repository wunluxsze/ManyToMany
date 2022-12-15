from django.db import models
from django.core.validators import MaxValueValidator


class Course(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Student(models.Model):
    name = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course, through='Enrollment')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    mark = models.IntegerField(validators=[MaxValueValidator(5)])

    class Meta:
        verbose_name = 'Зачисление'
        verbose_name_plural = 'Зачисления'


