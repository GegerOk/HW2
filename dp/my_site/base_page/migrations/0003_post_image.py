# Generated by Django 4.2.16 on 2024-10-19 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_page', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]