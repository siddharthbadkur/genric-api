from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


# ----------------------------------------------uSUAL MODEL
class StudentModel(models.Model):
    name=models.CharField(max_length=45)
    city=models.CharField(max_length=42)
    roll=models.IntegerField()

    def _str_(self):
        return self.name 
