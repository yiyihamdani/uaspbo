# Generated by Django 4.1.2 on 2022-10-28 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kelompok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=9)),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=50)),
                ('penulis', models.CharField(max_length=40)),
                ('penerbit', models.CharField(max_length=40)),
                ('jumlah', models.IntegerField(null=True)),
                ('kelompok_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_utspbo.kelompok')),
            ],
        ),
    ]
