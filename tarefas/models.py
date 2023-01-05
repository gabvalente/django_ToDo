from django.db import models


class Tarefas(models.Model):
    description = models.CharField(max_length=225)
    owner = models.CharField(max_length=100)
    duedate = models.DateField(blank=True, null=True)
    isdone = models.CharField(max_length=100)

    def __str__(self):
        return self.description
