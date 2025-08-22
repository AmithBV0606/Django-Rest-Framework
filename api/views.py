from django.http import JsonResponse
from students.models import Student

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
def studentsView(request):
    students = Student.objects.all()
    students_list = list(students.values())
    return JsonResponse(students_list, safe=False)
