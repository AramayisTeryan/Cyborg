# Generated by Django 4.1.6 on 2023-02-07 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_popularend'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Library name')),
                ('name1', models.CharField(max_length=50, verbose_name='Library name1')),
            ],
            options={
                'verbose_name': 'Library',
                'verbose_name_plural': 'Libraries',
            },
        ),
        migrations.AlterModelOptions(
            name='popularend',
            options={'verbose_name': 'PopularEnd', 'verbose_name_plural': 'PopularEnds'},
        ),
    ]