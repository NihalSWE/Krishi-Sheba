from django.db import models

# Create your models here.
class F_Data(models.Model):
    Name=models.CharField(max_length=100)
    Number=models.CharField(max_length=100)
    Email=models.EmailField()
    Details=models.TextField()
    

    def __str__(self):
        return self.Name