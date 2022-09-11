from django.urls import path
from . import views
  
urlpatterns = [
    path('create/', views.add_product, name='add-product'),
    path('list/', views.view_product, name='view_product'),
    path('update/<int:pk>/', views.update_product, name='update-product'),
    path('product/<int:pk>/delete/', views.delete_product, name='delete-product'),
]