from django.db import models
from django.db.models import ForeignKey
from mptt.models import MPTTModel, TreeForeignKey #Использовал данную библиотеку для создания древовидной структуры

#В этом файле описал модели Department и Employee


class Department(MPTTModel):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']
        level_attr = 'mptt_level'


class Employee(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    department = ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

