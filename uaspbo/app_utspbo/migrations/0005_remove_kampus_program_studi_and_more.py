# Generated by Django 4.1.2 on 2022-10-30 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_utspbo', '0004_nama_latin_jurnal_nama_latin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kampus',
            name='program_studi',
        ),
        migrations.RemoveField(
            model_name='kelompok_ikan',
            name='nama_latin',
        ),
    ]