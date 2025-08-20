from django.http import JsonResponse
from students.models import Student

# Create your views here.
def studentsView(request):
    # student = {
    #     'id': 1,
    #     'name': 'Amith',
    #     'class': 'CS'
    # }
    students = Student.objects.all()
    students_list = list(students.values())
    return JsonResponse(students_list, safe=False)