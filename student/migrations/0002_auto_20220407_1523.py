# Generated by Django 3.1.14 on 2022-04-07 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='matric_no',
            field=models.CharField(max_length=25),
        ),
    ]