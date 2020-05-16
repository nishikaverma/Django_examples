from django.db import models

class books(models.Model):
    book_id = models.IntegerField()
    book_name = models.TextField()
    book_price = models.FloatField()
    subject = models.CharField(max_length=30)
    publish_date = models.DateField(null=True) #thus giving publishing date is not compulsary now

    def __str__(self):
        return self.book_name



