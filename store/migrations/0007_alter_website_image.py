# Generated by Django 4.1.6 on 2023-02-15 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_website_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='image',
            field=models.ImageField(default=1, upload_to='static/images'),
            preserve_default=False,
        ),
    ]
