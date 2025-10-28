from django.db import migrations


def add_module_fisica(apps, schema_editor):
    Subject = apps.get_model('booking', 'Subject')
    Subject.objects.get_or_create(name='Módulo de Física')


def remove_module_fisica(apps, schema_editor):
    Subject = apps.get_model('booking', 'Subject')
    Subject.objects.filter(name='Módulo de Física').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_fix_course_levels'),
    ]

    operations = [
        migrations.RunPython(add_module_fisica, remove_module_fisica),
    ]
