import django_filters
from employees.models import Employee

# iexact - to make the search case insensitive

class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    id = django_filters.RangeFilter(field_name='id')
    # emp_id = django_filters.RangeFilter(field_name='emp_id') # - This won't work because the range filter only works on Integer fields

    class Meta:
        model = Employee
        fields = ['designation', 'emp_name', 'id']