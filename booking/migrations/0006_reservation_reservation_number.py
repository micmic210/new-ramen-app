# Generated by Django 4.2.16 on 2024-11-27 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_reservation_special_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='reservation_number',
            field=models.CharField(default='DEFAULT123', editable=False, max_length=10, unique=True),
        ),
    ]
