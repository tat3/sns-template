# Generated by Django 2.0.5 on 2018-06-30 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180630_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.CharField(default='', max_length=140),
        ),
    ]