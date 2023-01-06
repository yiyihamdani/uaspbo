# Generated by Django 4.1.2 on 2022-10-28 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_utspbo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jurnal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=60)),
                ('penulis', models.CharField(max_length=40)),
                ('penerbit', models.CharField(max_length=40)),
                ('email_penerbit', models.CharField(max_length=40)),
                ('tahun_terbit', models.IntegerField(null=True)),
                ('jumlah_halaman', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kampus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kampus', models.CharField(max_length=54)),
                ('program_studi', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Kelompok_ikan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_ikan', models.CharField(max_length=9)),
                ('nama_latin', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Buku',
        ),
        migrations.DeleteModel(
            name='Kelompok',
        ),
        migrations.AddField(
            model_name='jurnal',
            name='kampus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_utspbo.kampus'),
        ),
        migrations.AddField(
            model_name='jurnal',
            name='kelompok_ikan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_utspbo.kelompok_ikan'),
        ),
    ]
