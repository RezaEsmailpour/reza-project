# Generated by Django 2.1.7 on 2019-12-13 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='time',
            field=models.IntegerField(default=300),
            preserve_default=False,
        ),
    ]
