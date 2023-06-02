# Generated by Django 4.2.1 on 2023-05-30 21:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0014_alter_product_product_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_id",
            field=models.UUIDField(
                default=uuid.UUID("931d84b5-c64c-4765-81c6-4fbd455a8fa4"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
