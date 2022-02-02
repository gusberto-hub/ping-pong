# Generated by Django 3.0.3 on 2022-02-02 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_user_helper_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Member'), (2, 'Helper')], default=1),
        ),
    ]
