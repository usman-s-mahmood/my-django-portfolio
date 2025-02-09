from django.db import models

# Create your models here.

class Contact(models.Model):
    date_contacted = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False)
    subject = models.CharField(max_length=750, null=False, default='')
    message = models.TextField(null=False)

    def __str__(self):
        return str(f'{self.name} - <{self.date_contacted}>')
    