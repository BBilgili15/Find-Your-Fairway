from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Review, User

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
      "reviews": reviews,
      "reviews_count": range(5)
    }

    return render(request, 'courses/details.html', context)




# Takes you to physical "leave review" page
def leave_review(request, id):

    context = {
        "course": get_object_or_404(Course, id=id)
    }

    return render(request, 'courses/leave_review.html', context)





# BELOW IS HALF COOKED 

# View to actually add a review to the site
def add_review(request, id):
    if request.method == "POST":
        # Course == the course ID that you're already on 
        course = get_object_or_404(Course, id=id)
        # Description == what's written in input
        description = request.POST.get("description")
        # Reviewer == logged in user (but I have no login so need temporary workaround)
        reviewer = get_object_or_404(User, id=id) 
        # Rating == rating written 
        rating = request.POST.get("rating")
        # Date == today (how do I select today) - is below right?
        date = request.POST(auto_now_add=True)

        review = Review(course=course, description=description, reviewer=reviewer, rating=int(rating), date=date)
        review.save()
        return redirect(request.POST.get("redirect_url"))