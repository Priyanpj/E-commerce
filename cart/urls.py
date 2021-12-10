from django.urls import path
from.import views
urlpatterns=[
    path('cartdetials',views.cartdetials,name='cartdetials'),
    path('add/<int:pro_id>/',views.add_cart,name='addcart'),
    path('cart_decrement/<int:pro_id>/',views.min_cart,name='cart_decrement'),
    path('remove/<int:pro_id>/',views.cart_delete,name='remove'),


]