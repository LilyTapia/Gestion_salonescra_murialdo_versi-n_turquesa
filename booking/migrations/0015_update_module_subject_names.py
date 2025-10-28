from django.db import migrations


RENAME_MAP = {
    'Participación y argumentación en democracia': 'Módulo Participación y argumentación en democracia',
    'Comprensión histórica del presente': 'Módulo Comprensión histórica del presente',
    'Geografía, territorio y desafíos socioambientales': 'Módulo Geografía, territorio y desafíos socioambientales',
    'Probabilidades y estadísticas': 'Módulo Probabilidades y estadísticas',
    'Geometría 3D': 'Módulo Geometría 3D',
    'Ciencias de la salud': 'Módulo Ciencias de la salud',
    'Biología celular y molecular': 'Módulo Biología celular y molecular',
    'Ciencias del ejercicio físico y deportivo': 'Módulo Ciencias del ejercicio físico y deportivo',
    'Arquitectura y diseño': 'Módulo Arquitectura y diseño',
    'Interpretación musical': 'Módulo Interpretación musical',
    'Módulo de Física': 'Módulo Física',
}

CREATE_MODULE_NAMES = [
    'Módulo Física',
    'Módulo Química',
]


def forwards(apps, schema_editor):
    Subject = apps.get_model('booking', 'Subject')

    for old_name, new_name in RENAME_MAP.items():
        try:
            subject = Subject.objects.get(name=old_name)
        except Subject.DoesNotExist:
            continue
        if subject.name != new_name:
            subject.name = new_name
            subject.save(update_fields=['name'])

    for name in CREATE_MODULE_NAMES:
        Subject.objects.get_or_create(name=name)


def backwards(apps, schema_editor):
    Subject = apps.get_model('booking', 'Subject')

    reverse_map = {new: old for old, new in RENAME_MAP.items() if old not in ('Módulo de Física',)}
    for new_name, old_name in reverse_map.items():
        try:
            subject = Subject.objects.get(name=new_name)
        except Subject.DoesNotExist:
            continue
        if old_name:
            subject.name = old_name
            subject.save(update_fields=['name'])

    Subject.objects.filter(name__in=CREATE_MODULE_NAMES).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_add_module_fisica_subject'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
