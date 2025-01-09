# Generated by Django 4.2.17 on 2025-01-09 15:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0002_item_ingredients_item_nutritional_value_item_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="description",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="item",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name="item",
            name="size",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
