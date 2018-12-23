from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import login_view, registration_view, logout

app_name = 'authapp'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
    path('logout/', logout, name='logout'),
]