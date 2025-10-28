from django.db import migrations


def _infer_level_group(name):
    if not name:
        return 'BASICO'

    parts = name.strip().split()
    if len(parts) < 2:
        return 'BASICO'

    stage = parts[1].lower()
    first_token = parts[0]

    if stage != 'medio':
        return 'BASICO'

    digits = ''.join(ch for ch in first_token if ch.isdigit())
    if not digits:
        return 'MEDIO_3_4'

    try:
        level_number = int(digits)
    except ValueError:
        return 'MEDIO_3_4'

    return 'MEDIO_1_2' if level_number <= 2 else 'MEDIO_3_4'


def forwards(apps, schema_editor):
    Course = apps.get_model('booking', 'Course')
    for course in Course.objects.all():
        desired = _infer_level_group(course.name)
        if course.level_group != desired:
            course.level_group = desired
            course.save(update_fields=['level_group'])


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_add_jefe_utp_role'),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
