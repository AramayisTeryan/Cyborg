# Generated by Django 4.1.6 on 2023-02-08 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_browsemenu'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaruselHead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='CaruselHead name')),
            ],
            options={
                'verbose_name': 'CaruselHead',
                'verbose_name_plural': 'CaruselHeads',
            },
        ),
    ]
