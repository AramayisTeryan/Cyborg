# Generated by Django 4.1.6 on 2023-02-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_topfoot'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveStreamHead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='LiveStreamHead name')),
                ('name1', models.CharField(max_length=50, verbose_name='LiveStreamHead name1')),
            ],
            options={
                'verbose_name': 'LiveStreamHead',
                'verbose_name_plural': 'LiveStreamHeads',
            },
        ),
    ]