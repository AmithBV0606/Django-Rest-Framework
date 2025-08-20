from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def students(request):
    student = [
        {
            'id': 1,
            'name': "Amith",
            'age': 25
        }
    ]
    # return HttpResponse("<h2>Students Page!!</h2>")
    return HttpResponse(f'<h2>{student[0]}</h2>')