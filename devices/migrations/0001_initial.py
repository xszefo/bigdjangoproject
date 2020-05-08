# Generated by Django 3.0.5 on 2020-05-08 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('data_center', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='devices.DataCenter')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.Vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('ip_address', models.GenericIPAddressField()),
                ('unit', models.CharField(blank=True, max_length=2, null=True)),
                ('data_center', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='devices.DataCenter')),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='devices.Product')),
                ('rack', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='devices.Rack')),
            ],
        ),
    ]
