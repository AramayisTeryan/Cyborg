# Generated by Django 4.1.6 on 2023-02-09 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_streamscarusel'),
    ]

    operations = [
        migrations.CreateModel(
            name='StreamsTop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='StreamsTop name')),
                ('name1', models.CharField(max_length=50, verbose_name='StreamsTop name1')),
            ],
            options={
                'verbose_name': 'StreamsTop',
                'verbose_name_plural': 'StreamsTops',
            },
        ),
    ]
