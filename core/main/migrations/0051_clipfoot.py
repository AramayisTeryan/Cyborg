# Generated by Django 4.1.6 on 2023-02-11 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0050_clip'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClipFoot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='ClipFoot name')),
            ],
            options={
                'verbose_name': 'ClipFoot',
                'verbose_name_plural': 'ClipFoots',
            },
        ),
    ]
