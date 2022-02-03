# Generated by Django 3.0.3 on 2022-02-03 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0010_auto_20220203_1129'),
        ('user', '0016_auto_20220203_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='helper_sub_categories',
            field=models.ManyToManyField(blank=True, related_name='helper_category', to='category.SubCategory'),
        ),
    ]
