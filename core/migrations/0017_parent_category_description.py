# Generated by Django 2.2.4 on 2020-04-04 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20200322_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent_category',
            name='description',
            field=models.CharField(default='check', max_length=500),
            preserve_default=False,
        ),
    ]