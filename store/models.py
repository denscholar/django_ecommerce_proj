from django.db import models
from accounts.models import CustomUser
from django.utils.text import slugify
from django.urls import reverse
import uuid


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    # def get_absolute_url(self):
    #     return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    author = models.CharField(max_length=50, default="admin")
    image = models.ImageField(upload_to="images/")
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    product_id = models.UUIDField(
        default=uuid.uuid4(),
        primary_key=True,
        editable=False,
        unique=True,
    )
    slug = models.SlugField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = "Products"
        ordering = ("-created",)

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.product_id:
            self.product_id = uuid.uuid4()
        if not self.slug:
        # Combine the name and ID
            slug_text = f"{slugify(self.name)}-{str(self.product_id)}"
        # Generate a unique slug
            self.slug = slug_text
        return super().save(*args, **kwargs)
