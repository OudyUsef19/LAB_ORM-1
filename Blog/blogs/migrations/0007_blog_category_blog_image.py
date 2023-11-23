# Generated by Django 4.2.7 on 2023-11-23 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_alter_blog_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('Political', 'Political'), ('Sports', 'Sports'), ('Social', 'Social'), ('Technical', 'Technical')], default='Technical', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='imgs/default.jpg', upload_to='imgs/'),
        ),
    ]