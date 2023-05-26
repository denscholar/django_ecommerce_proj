from .models import Category


def show_categories(request):
    categories = Category.objects.all()
    return {
        "categories": categories,
    }
