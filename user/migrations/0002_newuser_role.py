# Generated by Django 4.0.3 on 2022-03-02 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='role',
            field=models.CharField(default='student', max_length=20),
        ),
    ]