# Generated by Django 5.0.6 on 2024-05-25 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_coures_is_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coures',
            name='author',
        ),
    ]
