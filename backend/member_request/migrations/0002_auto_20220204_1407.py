# Generated by Django 3.0.3 on 2022-02-04 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member_request', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberrequest',
            name='img_five',
        ),
        migrations.RemoveField(
            model_name='memberrequest',
            name='img_six',
        ),
    ]
