from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="information_home"),
    path('my-courses/<int:id>', views.my_courses, name="information_my_courses")
]
