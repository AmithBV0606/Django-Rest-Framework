from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# Routers (Viewsets) :
router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee') 
# No need of forward slash

urlpatterns = [
    # To get all the students at once :
    path('students/', views.studentsView),

    # To get an individual student at once :
    path('students/<int:pk>/', views.studentDetailView),

    # Employee App based routes :
    # path('employees/', views.Employees.as_view()),

    # To get an individual employee at once :
    # path('employees/<int:pk>', views.EmployeeDetails.as_view())

    # Routers :
    path('', include(router.urls)),

    # Blog and Commnets(Non-Primary) :
    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentsView.as_view()),
]
