from django.urls import path
from product.views import ProductListView,ProductDetailView,ProductByCategoryView
app_name = "product"

urlpatterns=[
    path('product-list/',ProductListView.as_view(),name="product_list"),
    path('<slug:category_slug>/<slug:product_slug>/', ProductDetailView.as_view(), name='product_detail'),
    # path('product-register/',ProductRegisterView.as_view(),name="product_register"),
    path('<slug:category_slug>/',ProductByCategoryView.as_view(),name="category_detail"),
    
    
]