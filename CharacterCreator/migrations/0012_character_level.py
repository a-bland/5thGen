# Generated by Django 3.1.7 on 2021-03-31 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CharacterCreator', '0011_auto_20210325_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='level',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
