# Generated by Django 4.1.6 on 2023-11-10 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactapp', '0002_remove_contact_phone_contact_contact_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
