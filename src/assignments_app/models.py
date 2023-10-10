from django.db import models
import uuid
import datetime

# Create your models here.
class Assignment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    time_cost = models.FloatField()
    priority = models.IntegerField()

    def __str__(self):
        return f"{self.label}"

class Status(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    types = [
        ('NEW', 'New'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done')
    ]
    status_type = models.CharField(max_length=12, choices=types, default='NEW')
    occurrence_time = models.DateTimeField(auto_now_add=True)
    assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="statuses")

    def __str__(self):
        return f"{self.status_type}"

class Developer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    pseudonym = models.CharField(max_length=100, unique=True)
    assignments_id = models.ManyToManyField(Assignment, through='Issue')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.pseudonym}"

class Issue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=200)
    description = models.TextField()
    developer_id = models.ForeignKey(Developer, on_delete=models.CASCADE)
    assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.label}"