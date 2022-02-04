# Generated by Django 3.0.3 on 2022-02-03 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0013_auto_20220203_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sub_categories',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='category.Category'),
        ),
    ]