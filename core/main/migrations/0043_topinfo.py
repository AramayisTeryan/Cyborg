# Generated by Django 4.1.6 on 2023-02-09 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_streamstop'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='TopInfo name')),
                ('about', models.TextField(verbose_name='TopInfo about')),
                ('number', models.IntegerField(verbose_name='TopInfo number')),
                ('img', models.ImageField(upload_to='media', verbose_name='TopInfo image')),
            ],
            options={
                'verbose_name': 'TopInfo',
                'verbose_name_plural': 'TopInfos',
            },
        ),
    ]
