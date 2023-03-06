from django.shortcuts import render, get_object_or_404
from .models import Course, Review

# Create your views here.
# def course(request, id):

#   print(Course.objects.get(id=id))

#   context = {
#     "course": get_object_or_404(Course, id=id),
#     "reviews": Review.objects.filter(course=id)
#   }

#   return render(request, 'courses/details.html', context)

def course(request, id):
    
    query_params = request.GET

    reviews = Review.objects.filter(course=id)

    filter_map = {
        "star-rating": "rating",
    }

    filters = {}
    for key, value in query_params.items():
        filter_key = filter_map[key]
        if value:
            filters[filter_key] = value

    reviews = reviews.filter(**filters)

    context = {
      "course": get_object_or_404(Course, id=id),
      "reviews": reviews
    }

    return render(request, 'courses/details.html', context)