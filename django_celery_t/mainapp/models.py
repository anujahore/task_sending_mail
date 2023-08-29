from django.db import models

# Create your models here.


class TestingEmp(models.Model):
    choices = (
        ("1", "Male"),
        ("2", "Female"),
    )
    name = models.CharField(max_length=50)
    email = models.EmailField()
    birthdate = models.DateField()
    Date_joined = models.DateField()
    gender = models.CharField(max_length=1, choices=choices)
    
    class Meta:
        db_table = "emptest"
        
    def __str__(self):
        return self.name
    
    