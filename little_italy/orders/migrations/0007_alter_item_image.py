# Generated by Django 4.2.17 on 2025-01-12 11:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0006_cart_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="image",
            field=models.URLField(blank=True, null=True),
        ),
    ]
