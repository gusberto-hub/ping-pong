# Generated by Django 3.0.3 on 2022-02-03 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0033_auto_20220203_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='code',
            field=models.CharField(default='56651', max_length=12),
        ),
    ]
