# Generated by Django 4.2.7 on 2023-11-22 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_alter_blog_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='is_published',
            field=models.BooleanField(default=0),
        ),
    ]