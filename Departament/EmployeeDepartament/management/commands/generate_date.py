from django.core.management.base import BaseCommand
from faker import Faker #Использовал библиотеку Faker(Генерация фальшивых данных)
import random
from EmployeeDepartament.models import Department, Employee


class Command(BaseCommand):
    help = 'Generate departments and employees'

    def handle(self, *args, **kwargs):
        fake = Faker('ru_RU')

        # Создание 25 подразделений с иерархией до 5 уровней
        root_department = Department.objects.create(name='Главный офис')
        for i in range(1, 26):
            department = Department.objects.create(name=f'Отдел {i}', parent=root_department)

        # Создание 50,000 сотрудников
        for _ in range(50000):
            Employee.objects.create(
                name=fake.name(),
                position=fake.job(),
                hire_date=fake.date_between(start_date='-5y'),
                salary=random.randint(30000, 200000),
                department=random.choice(Department.objects.all())
            )

