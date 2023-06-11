# Generated by Django 4.2.1 on 2023-06-10 23:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0006_alter_product_product_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_id",
            field=models.UUIDField(
                default=uuid.UUID("39d1c9ef-02c7-4108-b187-ae099fbc905f"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
