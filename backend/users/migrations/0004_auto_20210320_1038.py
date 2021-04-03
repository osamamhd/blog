# Generated by Django 3.1.7 on 2021-03-20 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210320_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailaddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_status', to=settings.AUTH_USER_MODEL),
        ),
    ]