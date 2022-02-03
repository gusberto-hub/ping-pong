# Generated by Django 3.0.3 on 2022-02-01 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import registration_profile.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationProfile',
            fields=[
                ('code', models.IntegerField(default=registration_profile.models.code_generator)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='registration_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
