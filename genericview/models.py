from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=40)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='skills')

    def __str__(self):
        return self.name
