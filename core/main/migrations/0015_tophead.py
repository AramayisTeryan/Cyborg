# Generated by Django 4.1.6 on 2023-02-08 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_carusel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopHead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='TopHead name')),
            ],
            options={
                'verbose_name': 'TopHead',
                'verbose_name_plural': 'TopHeads',
            },
        ),
    ]
