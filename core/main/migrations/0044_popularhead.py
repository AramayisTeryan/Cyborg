# Generated by Django 4.1.6 on 2023-02-10 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_topinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopularHead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='PopularHead name')),
                ('name1', models.CharField(max_length=50, verbose_name='PopularHead name1')),
            ],
            options={
                'verbose_name': 'PopularHead',
                'verbose_name_plural': 'PopularHeads',
            },
        ),
    ]