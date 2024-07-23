from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.CategoryListView.as_view(), name="category-list"),
    path("products/", views.ProductListView.as_view(), name="product-list"),
    path("products/<int:product_id>/", views.ProductDetailView.as_view(), name="product-detail"),
    path("categories/<int:category_id>/", views.CategoryDetailView.as_view(), name="category-detail"),
]
