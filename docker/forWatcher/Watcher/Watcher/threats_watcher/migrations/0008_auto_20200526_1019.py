# Generated by Django 3.0.6 on 2020-05-26 10:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('threats_watcher', '0003_auto_20200305_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='url',
            field=models.URLField(max_length=250),
        ),
    ]
