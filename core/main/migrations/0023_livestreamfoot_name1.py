# Generated by Django 4.1.6 on 2023-02-08 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_livestreamfoot'),
    ]

    operations = [
        migrations.AddField(
            model_name='livestreamfoot',
            name='name1',
            field=models.CharField(max_length=50, null=True, verbose_name='LiveStreamFoot name1'),
        ),
    ]
