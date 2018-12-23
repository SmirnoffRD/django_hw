from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import login_view, registration_view, logout, edit_view

app_name = 'authapp'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
    path('logout/', logout, name='logout'),
    path('edit/', edit_view, name='edit'),
]