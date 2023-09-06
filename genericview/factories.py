from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from genericview.models import Skill, Employee


class SkillFactory(DjangoModelFactory):
    name = Faker("name")

    class Meta:
        model = Skill


class EmployeeFactory(DjangoModelFactory):
    name = Faker("name")
    skill = SubFactory(SkillFactory)

    class Meta:
        model = Employee
