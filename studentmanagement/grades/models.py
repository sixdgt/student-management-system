from django.db import models

# Create your models here.
class Grade(models.Model):
    grade_name = models.CharField(max_length=255)
    grade_code = models.CharField(max_length=255)

    class Meta:
        db_table = 'sms_grades'
    
    def __str__(self):
        return self.grade_name