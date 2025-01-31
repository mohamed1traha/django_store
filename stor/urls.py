from django.urls import path,include
from .  import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:pid>', views.product, name='stor.product'),
    path('category/<int:cid>', views.category, name='stor.category'),
    path('category', views.category, name='stor.category'),
    path('cart', views.cart, name='stor.cart'),
    path('cart_update/<int:pid>', views.cart_update, name='stor.cart_update'),
    path('cart_remove/<int:pid>', views.cart_remove, name='stor.cart_remove'),
    path('checkout', views.checkout, name='stor.checkout'),
    path('checkout/complete', views.checkout_complete, name='stor.checkout_complete'),
]