# Generated by Django 3.2.12 on 2022-06-30 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0006_alter_problem_problemcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='problemcode',
        ),
    ]