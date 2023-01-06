# Generated by Django 4.1.2 on 2022-10-30 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_utspbo', '0003_alter_kelompok_ikan_nama_ikan_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='nama_latin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_latinn', models.CharField(max_length=54)),
            ],
        ),
        migrations.AddField(
            model_name='jurnal',
            name='nama_latin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_utspbo.nama_latin'),
        ),
    ]
