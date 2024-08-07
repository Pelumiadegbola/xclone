# Generated by Django 5.0.6 on 2024-07-17 19:21

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='annonymous', max_length=14, verbose_name='Name')),
                ('body', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Body')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='Image')),
                ('likes', models.PositiveIntegerField(blank=True, default=0, verbose_name='Likes')),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]
