"""courtyard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),  # 富文本编辑器
    path('docs/', get_swagger_view('API接口文档')),  # 接口文档
    path('', include('verifications.urls')),
    path('', include('users.urls')),
    path('oauth/', include('oauth.urls')),
    path('', include('areas.urls')),
    path('', include('goods.urls')),
    path('', include('content.urls')),
    path('', include('carts.urls')),
    path('orders/', include('orders.urls')),
    path('', include('payment.urls')),

]
