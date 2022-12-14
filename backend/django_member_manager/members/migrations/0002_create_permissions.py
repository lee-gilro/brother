

from django.db import migrations


def create_data(apps, schema_editor):
    permission = apps.get_model('members', 'Permission')
    permission(name="master").save()
    permission(name="diamond").save()
    permission(name="platinum").save()
    permission(name="gold").save()
    permission(name="silver").save()
    permission(name="bronze").save()


class Migration(migrations.Migration):
    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]

