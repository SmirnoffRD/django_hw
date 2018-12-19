"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from mainapp.views import contact_view, main_view, products_view
from mainapp.models import Category

categories = Category.objects.all()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main'),
    path('contacts/', contact_view, name='contacts'),
    path('products/', products_view, name='products'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


for category in categories:
    urlpatterns.append(path('products/{}/'.format(category.id), products_view, name='{}'.format(category.name)))


print(urlpatterns)