from django.db import models
import uuid

class Employee(models.Model):
    emp_name = models.CharField(max_length=200)
    emp_email = models.EmailField()
    emp_contact = models.CharField(max_length=20)
    emp_role = models.CharField(max_length=200)
    emp_salary = models.IntegerField()
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.emp_name