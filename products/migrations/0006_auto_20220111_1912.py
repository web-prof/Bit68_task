# Generated by Django 3.2.11 on 2022-01-11 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20220111_1851'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['prd_price']},
        ),
        migrations.AddField(
            model_name='products',
            name='prd_seller',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]