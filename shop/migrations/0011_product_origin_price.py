# Generated by Django 3.1 on 2020-10-17 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20201013_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='origin_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]