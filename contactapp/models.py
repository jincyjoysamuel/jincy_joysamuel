from django.db import models

class Contact(models.Model):
    serial_number = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=255)
    email = models.EmailField()
    notes = models.TextField(blank=True, null=True)  # New field for long paragraph
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.serial_number}: {self.contact_name} - {self.email}"
