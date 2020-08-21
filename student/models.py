from django.db import models
from repair import models as course_models
import uuid


def random_student_code():
    return uuid.uuid4().hex[:8].upper()


# Create your models here.
class Student(models.Model):
    student_id = models.SlugField(unique=True, default=random_student_code)
    course_id = models.ForeignKey(course_models.Repair, on_delete=models.CASCADE)
    #enroll_date = models.DateTimeField()
    #address = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    parent_contact = models.TextField()
