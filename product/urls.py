from django.urls import path, include
from .models import Product
from . import views
urlpatterns = [
    path('product/<int:pk>/', views.ProductMixinView.as_view(),
         name='product_description'),
    path('product/', views.ProductMixinView.as_view(), name="product_list"),
    path('product/<int:pk>/update/', views.ProductMixinView.as_view()),
    path('product/<int:pk>/delete/', views.ProductMixinView.as_view(),),
    path('',views.index)

]
