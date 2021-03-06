# Generated by Django 3.1.4 on 2021-02-06 07:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='dosen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fakultas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_fakultas', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='jurusan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_jurusan', models.CharField(max_length=50)),
                ('id_fakultas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.fakultas')),
            ],
        ),
        migrations.CreateModel(
            name='mahasiswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(blank=True, max_length=50, null=True)),
                ('judul', models.CharField(max_length=150)),
                ('abstrak', models.TextField(blank=True, null=True)),
                ('abstract', models.TextField(blank=True, null=True)),
                ('bab1', models.FileField(blank=True, null=True, upload_to=web.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['pdf']), web.models.file_size])),
                ('bab2', models.FileField(blank=True, null=True, upload_to=web.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['pdf']), web.models.file_size])),
                ('bab3', models.FileField(blank=True, null=True, upload_to=web.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['pdf']), web.models.file_size])),
                ('bab4', models.FileField(blank=True, null=True, upload_to=web.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['pdf']), web.models.file_size])),
                ('bab5', models.FileField(blank=True, null=True, upload_to=web.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['pdf']), web.models.file_size])),
                ('daftar_pustaka', models.FileField(blank=True, null=True, upload_to=web.models._upload_path, validators=[django.core.validators.FileExtensionValidator(['pdf']), web.models.file_size])),
                ('id_jurusan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='web.jurusan')),
                ('nim', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pembimbing1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pembimbing1', to='web.dosen')),
                ('pembimbing2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pembimbing2', to='web.dosen')),
            ],
        ),
        migrations.AddField(
            model_name='dosen',
            name='id_jurusan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='web.jurusan'),
        ),
        migrations.AddField(
            model_name='dosen',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
