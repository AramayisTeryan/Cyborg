# Generated by Django 4.1.6 on 2023-02-07 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_popular_name1'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopularImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='PopularImage name')),
                ('name1', models.CharField(max_length=50, verbose_name='PopularImage name1')),
                ('about', models.TextField(verbose_name='PopularImage about')),
                ('about1', models.TextField(verbose_name='PopularImage about1')),
                ('img', models.ImageField(upload_to='media', verbose_name='PopularImage image')),
            ],
            options={
                'verbose_name': 'PopularImage',
                'verbose_name_plural': 'PopularImages',
            },
        ),
    ]
