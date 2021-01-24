from django.urls import path

from .views import products, ProductsList, product_detail, SearchProductsView, ProductsListByCategory, products_categories_partial

urlpatterns = [
    path('products-fbv', products),
    path('products-cbv', ProductsList.as_view()),  # do not forget to add .as_view method at the end of class name
    # when using class-based views
    # path('products-detail', product_detail),
    path('products/<productId>/<name>', product_detail),
    path('products/search', SearchProductsView.as_view()),
    path('products/<category_name>', ProductsListByCategory.as_view()),
    path('products_categories_partial', products_categories_partial, name='products_categories_partial')

]
