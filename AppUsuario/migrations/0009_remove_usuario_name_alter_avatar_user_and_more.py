# Generated by Django 4.1.3 on 2022-12-22 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppUsuario', '0008_albumimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='name',
        ),
        migrations.AlterField(
            model_name='avatar',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppUsuario.usuario'),
        ),
        migrations.DeleteModel(
            name='AlbumImage',
        ),
    ]
