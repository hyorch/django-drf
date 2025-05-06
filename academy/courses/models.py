from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    

    def __str__(self):
        return f"{self.id} {self.name} {self.description} {self.rating}"
