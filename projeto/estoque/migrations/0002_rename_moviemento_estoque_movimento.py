# Generated by Django 4.2.1 on 2023-05-08 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estoque',
            old_name='moviemento',
            new_name='movimento',
        ),
    ]
