# Generated by Django 2.2.4 on 2020-03-15 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_article_slug1'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent_category',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
