# Generated by Django 3.0.3 on 2022-02-02 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20220202_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helperprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='memberprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='helper_profile',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.HelperProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='member_profile',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.MemberProfile'),
            preserve_default=False,
        ),
    ]
