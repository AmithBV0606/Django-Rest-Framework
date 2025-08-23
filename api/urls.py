from django.urls import path, include
from . import views

urlpatterns = [
    # To get all the students at once :
    path('students/', views.studentsView),

    # To get an individual student at once :
    path('students/<int:pk>/', views.studentDetailView),

    # Employee App based routes :
    path('employees/', views.Employees.as_view())
]
