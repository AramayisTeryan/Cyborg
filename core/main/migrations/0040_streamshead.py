# Generated by Django 4.1.6 on 2023-02-09 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_streamsmenu'),
    ]

    operations = [
        migrations.CreateModel(
            name='StreamsHead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='StreamsHead name')),
                ('name1', models.CharField(max_length=50, verbose_name='StreamsHead name1')),
            ],
            options={
                'verbose_name': 'StreamsHead',
                'verbose_name_plural': 'StreamsHeads',
            },
        ),
    ]
