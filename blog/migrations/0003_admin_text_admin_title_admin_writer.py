# Generated by Django 4.1.6 on 2023-02-14 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_new_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='text',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='admin',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='admin',
            name='writer',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
