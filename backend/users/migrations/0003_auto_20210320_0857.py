# Generated by Django 3.1.7 on 2021-03-20 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210320_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailconfirmation',
            name='key',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
