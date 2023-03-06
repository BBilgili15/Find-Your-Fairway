from . import views
from django.urls import path

urlpatterns = [
    # path('', views.XXXXX, name=""),
    path("details/<int:id>", views.course, name="course_details")
]
