from django.test import TestCase
from store.models import Category, Product
from django.contrib.auth.models import User


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name="javascript", slug="javascript")

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes

        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_name(self):
        data = self.data1
        self.assertEqual(str(data), "javascript")


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name="javascript", slug="javascript")
        User.objects.create(username="admin")
        self.data1 = Product.objects.create(
            category_id=1,
            title="javascript for beginners",
            description="This is a javascript course",
            created_by_id=1,
            slug="javascript",
            price="200.00",
            image="django.png",
        )

    def test_product_model_entry(self):
        """
        Test Product model data insertion/types/field attributes

        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), "javascript for beginners")
