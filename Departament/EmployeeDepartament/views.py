
from django.views.generic import ListView
from .models import Department


class DepartmentTreeView(ListView):
    template_name = 'departments/main.html'
    queryset = Department.objects.all()
    context_object_name = 'departments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context