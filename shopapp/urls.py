from django.urls import path
from.import views
urlpatterns=[
    path('',views.fun,name='fun'),
    path('blog/', views.blogs, name='blogs'),
    path('contact/',views.contact,name='contact'),
    path('blogs/', views.blogs, name='blogs'),
    path('shop/',views.shop,name='shop'),
    path('add/',views.add_product,name='add_product'),
    path('update/<int:id>',views.update,name='update'),
    path('add/proupdate/',views.proadd,name='proadd'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('<slug:c_slug>/',views.fun,name='prod_cat'),
    path('search',views.searching,name='search'),







    # path('/feature_products/<int:pro_id>',views.detial,name='detial')
    # path('',views.fan,name='fan'),

]