from django.urls import path
from interface import views

urlpatterns = [
    path('', views.home, name='home'),
    path('assistance', views.assistance, name='assistance'),
    path('can_assist', views.can_assist, name='can-assist'),
    path('success', views.success, name='success')
]