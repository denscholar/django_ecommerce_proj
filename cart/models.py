# from django.db import models

# from django.contrib.auth.models import User
# from store.models import Product


# # class Cart(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     created_at = models.DateTimeField(auto_now_add=True)


# #     def __str__(self):
# #         return self.user.username

# #     # objects = models.Manager()  # Add the objects attribute
# #     def calculate_total_price(self):
# #         total_price = 0
# #         for item in self.items.all():
# #             total_price += item.product.price * item.quantity
# #         return total_price


# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(null=False, blank=False)
#     created_at = models.DateTimeField(auto_now_add=False)

#     def __str__(self):
#         return self.product.name
