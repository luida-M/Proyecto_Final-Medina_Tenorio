# Generated by Django 5.1.4 on 2025-01-14 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_formcliente_proyecto_rename_name_cliente_nombre_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='company',
            new_name='empresa',
        ),
    ]