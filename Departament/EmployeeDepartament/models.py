from django.db import models
from django.db.models import ForeignKey
from mptt.models import MPTTModel, TreeForeignKey #Использовал данную библиотеку для создания древовидной структуры
from django.core.exceptions import ValidationError

#В этом файле описал модели Department и Employee


class Department(MPTTModel):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']
        level_attr = 'mptt_level'

    class Meta:
        unique_together = ('name', 'parent')

    def __str__(self):
        return self.name


def clean(self):
    # Проверка вложенности при сохранении через админку
    if self.parent:
        if self.parent.level >= 4:
            raise ValidationError(
                f"Невозможно создать департамент 6-го уровня. "
                f"Текущая вложенность: {self.parent.level + 1}/5"
            )
    return super().clean()


def save(self, *args, **kwargs):
    # Принудительная валидация при сохранении
    self.full_clean()
    super().save(*args, **kwargs)


class Employee(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    department = ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.name