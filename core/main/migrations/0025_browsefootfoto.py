# Generated by Django 4.1.6 on 2023-02-08 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_browsefoothead'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrowseFootFoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='BrowseFootFoto name')),
                ('about', models.TextField(verbose_name='BrowseFootFoto about')),
                ('about1', models.TextField(verbose_name='BrowseFootFoto about1')),
                ('about2', models.TextField(verbose_name='BrowseFootFoto about2')),
                ('about3', models.TextField(verbose_name='BrowseFootFoto about3')),
                ('img', models.ImageField(upload_to='media', verbose_name='BrowseFootFoto image')),
                ('img1', models.ImageField(upload_to='media', verbose_name='BrowseFootFoto image1')),
            ],
            options={
                'verbose_name': 'BrowseFootFoto',
                'verbose_name_plural': 'BrowseFootFotos',
            },
        ),
    ]
