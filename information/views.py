from django.shortcuts import render, get_object_or_404
from courses.models import Course, UserProfile, User
from django.contrib.auth.models import User

# Create your views here.
def home(request):

    query_params = request.GET

    filter_map = {
        "query": "name__icontains",
        "par": "par"
    }

    filters = {}
    for key, value in query_params.items():
        filter_key = filter_map[key]
        if value:
            filters[filter_key] = value

    courses = Course.objects.filter(**filters)

    context = {
        "courses": courses
    }

    return render(request, 'information/home.html', context)


def my_courses(request, id):

    context = {
        "user": get_object_or_404(User, id=id),
        "courses": Course.objects.all()
    }

    return render(request, 'information/my_courses.html', context)