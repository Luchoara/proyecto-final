# Generated by Django 4.1.3 on 2022-12-11 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppUsuario', '0002_avatar_postcriticas_posteo_postnoticias_delete_login'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PostCriticas',
        ),
        migrations.DeleteModel(
            name='PostNoticias',
        ),
    ]
