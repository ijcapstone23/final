"""
URL configuration for price_comparison_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from search import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.search, name='search'),
    path('result/<str:q>/', views.result, name='result'),
    path('result/<str:q>/<int:page>/', views.result2, name='result2'),
    path('adv/<str:q>/', views.result3, name='result3'),
    path('index/', views.index, name='index'),
#    path('results/', views.results, name='results'),
#    path('item/<int:product_id_id>/', views.detail, name='detail'),
]
