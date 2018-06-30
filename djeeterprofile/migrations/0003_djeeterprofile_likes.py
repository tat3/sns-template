# Generated by Django 2.0.5 on 2018-06-30 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djeet', '0002_djeet_user'),
        ('djeeterprofile', '0002_djeeterprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='djeeterprofile',
            name='likes',
            field=models.ManyToManyField(related_name='liked_by', to='djeet.Djeet'),
        ),
    ]
