from django.urls import path
from . import views

urlpatterns = [
      path('demo', views.showDemoPage),
      path('', views.ShowLoginPage, name="show_login"),
      path('get_user_details', views.GetUserDetails),
      path('logout_user', views.logout_user, name="logout"),
      path('doLogin', views.doLogin, name="do_login"),
]