# Generated by Django 2.0.5 on 2018-07-03 11:30

from django.db import migrations


def apply_migration(apps, schema_editor):
    """Create group feature.templates"""
    Group = apps.get_model('auth', 'Group')
    Group.objects.create(name='feature.templates')


def revert_migration(apps, schema_editor):
    """Remove group feature.templates"""
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name='feature.templates').delete()


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.RunPython(apply_migration, revert_migration)
    ]
