# Generated by Django 3.2.11 on 2022-01-08 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220108_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='prd_image',
            field=models.ImageField(blank=True, null=True, upload_to='prd_images/'),
        ),
    ]
