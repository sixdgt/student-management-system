from django.urls import path
from . import views 
urlpatterns = [
    path('', views.student_index, name="students"),
]