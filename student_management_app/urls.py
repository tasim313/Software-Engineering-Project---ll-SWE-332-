from django.urls import path
from . import views

urlpatterns = [
      path('demo', views.showDemoPage),
      path('', views.ShowLoginPage, name="show_login"),
]