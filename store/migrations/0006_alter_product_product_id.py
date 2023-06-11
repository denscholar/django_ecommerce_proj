# Generated by Django 4.2.1 on 2023-06-10 23:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0005_alter_product_product_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_id",
            field=models.UUIDField(
                default=uuid.UUID("a4ffa2d4-cfc5-43eb-96f7-66a71a5de242"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
