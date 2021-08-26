from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='index'),
    path('post/',views.post_detail,name='post'),
    path('student/',views.student,name='student'),
    path('teacher/',views.teacher,name='teacher'),
    path('admins/',views.admins,name='admins'),
    path('contact/',views.contactus,name='contactus'),
    path('about/',views.aboutus,name='about'),
    path('post_detail/<int:id>/',views.post_detail,name='post_detail'),
    path('student_detail/<int:id>/',views.student_detail,name='student_detail'),
    path('teacher_detail/<int:id>/',views.teacher_detail,name='teacher_detail'),

]