from django.views.generic import ListView
from .models import Department, Employee


class DepartmentTreeView(ListView):
    template_name = 'departments/main.html'
    queryset = Department.objects.all()
    context_object_name = 'departments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.select_related('department').all() # Решение избыточных данных в БД
        return context