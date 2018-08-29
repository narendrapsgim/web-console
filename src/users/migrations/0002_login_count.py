# Generated by Django 2.0.5 on 2018-08-10 15:54

from django.db import migrations, models


def forwards_func(apps, schema_editor):
    """
    Change login counter for users who already logged in so they don't trigger
    registered event
    """
    Profile = apps.get_model('users', 'Profile')
    Profile.objects.filter(user__last_login__isnull=False).update(login_count=1)


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='login_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.RunPython(forwards_func, reverse_func),
    ]