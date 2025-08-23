from django.http import JsonResponse
from students.models import Student


from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from employees.models import Employee
from .serializers import EmployeeSerializer, StudentSerializer

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

@api_view(['GET', 'POST'])
def studentsView(request):
    # Fetch data
    if request.method == "GET":
        students = Student.objects.all() # Query Set
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST": # Store data
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def studentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Get A Single Object Primary Key-Based Operation
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # Update Operation on Student(PUT) :
    elif request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Delete Operation on Student(DELETE) :
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Class based views demo :

class Employees(APIView):
    def get(self, request): # Member function instance method
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)