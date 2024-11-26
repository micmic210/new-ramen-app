# Generated by Django 4.2.16 on 2024-11-26 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('superadmin', 'Super Admin'), ('manager', 'Manager'), ('staff', 'Staff')], default='staff', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]