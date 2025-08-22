from django.http import JsonResponse
from students.models import Student

from .serializers import StudentSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Static Data JSON response :
# def studentsView(request):
#     # student = {
#     #     'id': 1,
#     #     'name': 'Amith',
#     #     'class': 'CS'
#     # }
#     return JsonResponse(student)

# Dynamic data coming from DB as JSON response : This won't work
# def studentsView(request):
#     students = Student.objects.all()
#     return JsonResponse(students, safe=False)

# Manual Serialization : Converting the Query Set into the list
# def studentsView(request):
#     students = Student.objects.all()
#     students_list = list(students.values())
#     return JsonResponse(students_list, safe=False)

# NOTE : If you want your view to be accessed by only specific request type, we can use "api_view"

@api_view(['GET'])
def studentsView(request):
    if request.method == "GET":
        students = Student.objects.all() # Query Set
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
