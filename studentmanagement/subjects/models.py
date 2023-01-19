from django.db import models
from grades.models import Grade

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
    subject_code = models.CharField(max_length=255)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    class Meta:
        db_table = 'sms_subjects'
    
    def __str__(self):
        return self.subject_name