# Generated by Django 3.0.3 on 2022-02-03 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0037_auto_20220203_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='code',
            field=models.CharField(default='75428', max_length=12),
        ),
    ]
