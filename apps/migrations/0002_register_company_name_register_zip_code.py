# Generated by Django 5.1.1 on 2024-09-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='company_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='zip_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
