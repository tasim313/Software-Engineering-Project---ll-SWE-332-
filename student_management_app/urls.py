from django.urls import path
from . import views
from . import adminviews
urlpatterns = [
      path('demo', views.showDemoPage),
      path('', views.ShowLoginPage, name="show_login"),
      path('get_user_details', views.GetUserDetails),
      path('logout_user', views.logout_user, name="logout"),
      path('doLogin', views.doLogin, name="do_login"),
      path('admin_home',     adminviews.admin_home, name="admin_home"),
      path('manage_teacher', adminviews.manage_teacher, name="manage_teacher"),
      path('manage_student', adminviews.manage_student, name="manage_student"),
      path('manage_course',  adminviews.manage_course, name="manage_course"),
      path('manage_subject', adminviews.manage_subject, name="manage_subject"),
]