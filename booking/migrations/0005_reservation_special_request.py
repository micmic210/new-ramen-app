# Generated by Django 4.2.16 on 2024-11-27 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_contactmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='special_request',
            field=models.TextField(blank=True, null=True),
        ),
    ]