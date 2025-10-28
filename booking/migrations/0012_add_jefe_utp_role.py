from django.db import migrations


def add_jefe_utp_role(apps, schema_editor):
    TeacherRole = apps.get_model('booking', 'TeacherRole')
    TeacherRole.objects.get_or_create(name='Jefe/a UTP de ciclo')


def remove_jefe_utp_role(apps, schema_editor):
    TeacherRole = apps.get_model('booking', 'TeacherRole')
    TeacherRole.objects.filter(name='Jefe/a UTP de ciclo').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_alter_course_level_group'),
    ]

    operations = [
        migrations.RunPython(add_jefe_utp_role, remove_jefe_utp_role),
    ]
