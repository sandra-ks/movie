# Generated by Django 4.2.5 on 2023-09-13 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='dfff', upload_to='gallery'),
            preserve_default=False,
        ),
    ]