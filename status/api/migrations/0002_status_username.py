# Generated by Django 4.1 on 2022-08-25 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]