from django.db import models

class Contact(models.Model):
    serial_number = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.serial_number}: {self.email}"
