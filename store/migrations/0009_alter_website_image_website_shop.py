# Generated by Django 4.1.6 on 2023-02-15 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_admin_image'),
        ('store', '0008_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Website_Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_title', models.CharField(max_length=150, null=True)),
                ('title', models.CharField(max_length=250, null=True)),
                ('text', models.TextField(max_length=300, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.admin')),
            ],
        ),
    ]