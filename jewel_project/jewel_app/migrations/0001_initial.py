# Generated by Django 5.1.4 on 2024-12-20 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_id', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('a_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='article_images/img')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('author', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(choices=[('P', 'Published'), ('U', 'Unpublished')], default='U', max_length=1)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('views_count', models.IntegerField(default=0)),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jewel_app.categories')),
            ],
        ),
    ]
