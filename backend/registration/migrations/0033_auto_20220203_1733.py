# Generated by Django 3.0.3 on 2022-02-03 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0032_auto_20220203_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='code',
            field=models.CharField(default='38515', max_length=12),
        ),
    ]
