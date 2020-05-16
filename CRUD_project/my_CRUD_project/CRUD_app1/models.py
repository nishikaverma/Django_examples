from django.db import models

class Employee(models.Model):
    e_id = models.IntegerField()
    e_name = models.CharField(max_length=30)
    e_mail = models.EmailField()
    e_sal = models.FloatField()    

    def __str__(self):
        return self.e_name