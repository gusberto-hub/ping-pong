# Generated by Django 3.0.3 on 2022-02-03 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20220203_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='code',
            field=models.CharField(default='97216', max_length=12),
        ),
    ]