# Generated by Django 4.1.6 on 2023-02-09 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=2, upload_to='static/image/images'),
            preserve_default=False,
        ),
    ]