# Generated by Django 4.1.6 on 2023-02-08 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_livestreamhead'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveStreamBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='LiveStreamBody name')),
                ('about', models.TextField(verbose_name='LiveStreamBody about')),
                ('about1', models.TextField(verbose_name='LiveStreamBody about1')),
                ('img', models.ImageField(upload_to='media', verbose_name='LiveStreamBody image')),
            ],
            options={
                'verbose_name': 'LiveStreamBody',
                'verbose_name_plural': 'LiveStreamBodies',
            },
        ),
    ]
