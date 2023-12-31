# Generated by Django 4.2.3 on 2023-07-22 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='direccionUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(blank=True, max_length=32, null=True)),
                ('region', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='infousuarios',
            name='direccionInfo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app2.direccionusuario'),
        ),
    ]
