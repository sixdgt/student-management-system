from . import views
from django.urls import path

urlpatterns = [
    path('students/detail/<int:pk>', views.student_detail, name='students.details'),
    path('students/', views.student_list, name='students.list'),
]