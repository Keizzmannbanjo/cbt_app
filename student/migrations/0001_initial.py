# Generated by Django 4.0.5 on 2023-02-19 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lecturer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=25)),
                ('first_name', models.CharField(max_length=25)),
                ('other_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=100)),
                ('matric_no', models.CharField(max_length=25)),
                ('session_type', models.CharField(choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time')], max_length=15)),
                ('level', models.CharField(choices=[('ND1', 'ND1'), ('ND2', 'ND2'), ('ND3', 'ND3'), ('HND1', 'HND1'), ('HND2', 'HND2'), ('HND3', 'HND3')], max_length=4)),
                ('subjects', models.ManyToManyField(related_name='students', to='lecturer.subject')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
