# Generated by Django 3.0.3 on 2022-02-03 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0028_auto_20220203_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='code',
            field=models.CharField(default='16181', max_length=12),
        ),
    ]
