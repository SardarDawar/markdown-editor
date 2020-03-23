# Generated by Django 2.2.4 on 2020-03-07 19:56

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191220_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=500)),
                ('slug', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Parent_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=500)),
                ('slug', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Parent Categories',
            },
        ),
        migrations.RenameField(
            model_name='profilemodel',
            old_name='level1',
            new_name='writer',
        ),
        migrations.RemoveField(
            model_name='profilemodel',
            name='level2',
        ),
        migrations.RemoveField(
            model_name='profilemodel',
            name='level3',
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='regular_user',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=500)),
                ('slug', models.CharField(max_length=500)),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
            ],
            options={
                'verbose_name_plural': 'Subcategories',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='Parent_Category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Parent_Category'),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('slug', models.CharField(max_length=1000)),
                ('status', models.CharField(choices=[('published', 'Published'), ('draft', 'draft')], max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('description', mdeditor.fields.MDTextField()),
                ('Date', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('bottom', models.BooleanField(default=True)),
                ('search_vector', django.contrib.postgres.search.SearchVectorField(blank=True, null=True)),
                ('Parent_Category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Parent_Category')),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
                ('sub_catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Sub_Category')),
            ],
            options={
                'ordering': ['-Date', '-updated'],
            },
        ),
        migrations.AddIndex(
            model_name='article',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='core_articl_search__874a34_gin'),
        ),
    ]
