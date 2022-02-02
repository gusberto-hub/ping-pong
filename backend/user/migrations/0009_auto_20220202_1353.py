# Generated by Django 3.0.3 on 2022-02-02 13:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20220202_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='helper_profile',
        ),
        migrations.RemoveField(
            model_name='user',
            name='member_profile',
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='helper_available',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='user',
            name='helper_available_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='helper_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='MemberProfile',
        ),
    ]