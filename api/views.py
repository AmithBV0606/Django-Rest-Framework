from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def studentsView(request):
    student = {
        'id': 1,
        'name': 'Amith',
        'class': 'CS'
    }
    return JsonResponse(student)