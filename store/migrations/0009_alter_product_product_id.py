# Generated by Django 4.2.1 on 2023-06-13 09:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0008_rename_name_product_prod_name_remove_product_author_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_id",
            field=models.UUIDField(
                default=uuid.UUID("1571539c-4d2e-43dc-a91e-ae5d0199da01"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
