
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views,Hod_views,Staff_views,Student_views



urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('base/', views.BASE, name='base'),
                  # login path
                  path('', views.LOGIN, name='login'),
                  path('doLogin', views.doLogin, name='doLogin'),
                  path('doLogout', views.doLogout, name='logout'),
                  # profile update
                  path('Profile', views.PROFILE, name='profile'),
                  path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),
                  # This is HOD Pannal
                  #Student
                  path('HOD/home', Hod_views.HOME, name='hod_home'),
                  path('HOD/Student/Add',Hod_views.ADD_STUDENT,name='add_student'),
                  path('HOD/Student/View',Hod_views.VIEW_STUDENT,name='view_student'),
                  path('HOD/Student/Edit/<str:id>',Hod_views.EDIT_STUDENT,name='edit_student'),
                  path('HOD/Student/Update',Hod_views.UPDATE_STUDENT,name='update_student'),
                  path('HOD/Student/Delete/<str:admin>',Hod_views.DELETE_STUDENT,name='delete_student'),

                  #Staff
                  path('Hod/Staff/Add',Hod_views.ADD_STAFF,name='add_staff'),
                  path('Hod/Staff/View',Hod_views.VIEW_STAFF,name='view_staff'),
                  path('Hod/Staff/Edit<str:id>',Hod_views.EDIT_STAFF,name='edit_staff'),
                  path('Hod/Staff/Update',Hod_views.UPDATE_STAFF,name='update_staff'),
                  path('Hod/Staff/Delete<str:admin>',Hod_views.DELETE_STAFF,name='delete_staff'),

                  #Branch
                  path('HOD/Branch/Add',Hod_views.ADD_BRANCH,name='add_branch'),
                  path('HOD/Branch/View',Hod_views.VIEW_BRANCH,name='view_branch'),
                  path('HOD/Branch/Edit/<str:id>',Hod_views.EDIT_BRANCH,name='edit_branch'),
                  path('HOD/Branch/Update',Hod_views.UPDATE_BRANCH,name='update_branch'),
                  path('HOD/Branch/Delete/<str:id>',Hod_views.DELETE_BRANCH,name='delete_branch'),

                  #Subject

                  path('Hod/Subject/Add',Hod_views.ADD_SUBJECT,name='add_subject'),
                  path('Hod/Subject/View',Hod_views.VIEW_SUBJECT,name='view_subject'),
                  path('Hod/Subject/Edit/<str:id>',Hod_views.EDIT_SUBJECT,name='edit_subject'),
                  path('Hod/Subject/Update',Hod_views.UPDATE_SUBJECT,name='update_subject'),
                  path('Hod/Subject/Delete<str:id>',Hod_views.DELETE_SUBJECT,name= 'delete_subject'),
                  path('Hod/Staff/Send_Notification',Hod_views.STAFF_SEND_NOTIFICATION,name= 'staff_send_notification'),
                  path('Hod/Staff/save_notification',Hod_views.SAVE_STAFF_NOTIFICATION,name='save_staff_notification'),
                  path('Hod/Student/Notifications',Hod_views.STUD_NOTIFICATIONS,name='stud_notifications'),
                  path('Hod/Student/Student_save_notification',Hod_views.SAVE_STUD_NOTI,name='save_stud_noti'),
                  path('Hod/Student/Feedback',Hod_views.STUDENT_FEEDBACK,name='student_feedback'),
                  path('Hod/Student/Feedback/reply',Hod_views.F_REPLY,name='f_reply'),


                  #student urls
                  path('student/home',Student_views.HOME,name='home'),
                  path('Student/Notifications',Student_views.S_NOTIFICATIONS,name='s_notifications'),
                  path('Student/mark_noti/<str:status>',Student_views.MARK_NOTI,name= 'mark_noti'),
                  path('Student/feedback',Student_views.STUDENT_FEED,name= 'student_feed'),
                  path('Student/feedback/save', Student_views.SAVE_FEEDBACK, name='save_feedback'),
                  path('Student/view_result',Student_views.VIEW_RESULT,name= 'view_result'),

                  #staff urls
                  path('staff/Home',Staff_views.HOME,name='staff_home'),
                  path('Staff/Notifications',Staff_views.NOTIFICATIONS,name='notifications'),
                  path('Staff/mark_as_done/<str:status>',Staff_views.MARK_NOTIFICATION,name='mark_notification'),
                  path('Staff/Take_Attendance',Staff_views.STAFF_TAKE_ATTEND,name='staff_take_attend'),
                  path('Staff/Save_attendance',Staff_views.STAFF_SAVE_ATTENDANCE,name='staff_view_attendance'),
                  path('Staff/Add/Result',Staff_views.STAFF_ADD_RESULT,name='staff_add_result'),
                  path('Staff/Save/Result',Staff_views.STAFF_SAVE_RES,name='staff_save_res'),

              ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
