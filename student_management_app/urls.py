from django.urls import path
from . import views
from . import adminviews, teacherviews, Studentviews
urlpatterns = [
      path('demo', views.showDemoPage),
      path('', views.ShowLoginPage, name="show_login"),
      path('get_user_details', views.GetUserDetails),
      path('logout_user', views.logout_user, name="logout"),
      path('doLogin', views.doLogin, name="do_login"),
      path('admin_home',     adminviews.admin_home,     name="admin_home"),
      path('add_student',    adminviews.add_student,    name='add_student'),
      path('add_course',     adminviews.add_course,     name='add_course'),
      path('add_subject',    adminviews.add_subject,    name='add_subject'),
      path('add_teacher',    adminviews.add_teacher,    name='add_teacher'),
      path('add_teacher_save', adminviews.add_teacher_save, name="add_teacher_save"),
      path('manage_teacher', adminviews.manage_teacher, name="manage_teacher"),
      path('manage_student', adminviews.manage_student, name="manage_student"),
      path('manage_course',  adminviews.manage_course,  name="manage_course"),
      path('manage_subject', adminviews.manage_subject, name="manage_subject"),
      path('edit_teacher/<str:teacher_id>', adminviews.edit_teacher, name="edit_teacher"),
      path('edit_teacher_save', adminviews.edit_teacher_save, name="edit_teacher_save"),

      # Teacher urls
      path('teacher_home', teacherviews.teacher_home, name="teacher_home"),

      # student urls
      path('student_home', Studentviews.student_home, name="student_home"),
]