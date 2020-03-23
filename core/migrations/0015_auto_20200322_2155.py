# Generated by Django 2.2.4 on 2020-03-22 16:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0014_auto_20200322_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent_category',
            name='Private_Users',
        ),
        migrations.AddField(
            model_name='parent_category',
            name='Private',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]