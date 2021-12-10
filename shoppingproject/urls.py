"""shoppingproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from shopapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shopapp.urls')),
    path('cart/',include('cart.urls')),
    path('accounts/',include('accounts.urls')),
    path('feature_products/<int:pro_id>',views.detial,name='detial'),
    # path('feature_products/<int:pro_id>',views.detial,name='detiall'),
    path('feature_products/<int:pro_id>', views.detials, name='detials'),
    path('feature_products/<int:pro_id>',views.blog,name='blog'),
    # path('feature_products/<int:pro_id>',views.filter,name='filter')
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_ROOT,
                          document_root = settings.MEDIA_ROOT)