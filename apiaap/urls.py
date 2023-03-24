from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('stuinfo/<int:pk>',views.Student_detail),
    path('stuinfo/',views.student_list),
    
]
