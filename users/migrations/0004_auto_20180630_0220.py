# Generated by Django 2.0.5 on 2018-06-30 02:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180630_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='unknown', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 10 characters or fewer. Letters, digits and _ only.', max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^[\\w]+$', 'Enter a valid username. This value may contain only letters, numbers and _ characters.', 'invalid')], verbose_name='username'),
        ),
    ]
