# Generated by Django 4.2.1 on 2023-05-29 16:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0006_alter_product_managers_product_is_active_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_id",
            field=models.UUIDField(
                default=uuid.UUID("1b8ddad1-70f9-4256-be9f-4171438d9cad"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
