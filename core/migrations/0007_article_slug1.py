# Generated by Django 2.2.4 on 2020-03-15 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200315_0648'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug1',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
