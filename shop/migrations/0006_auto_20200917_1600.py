# Generated by Django 3.1 on 2020-09-17 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0005_buyinglist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyinglist',
            name='buylist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buylists', to=settings.AUTH_USER_MODEL),
        ),
    ]
