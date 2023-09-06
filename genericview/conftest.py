import pytest
from genericview.factories import SkillFactory, EmployeeFactory
from genericview.models import Skill, Employee
from rest_framework.test import APIClient


@pytest.fixture
def create_skill() -> Skill:
    factory = SkillFactory.create()
    return factory


@pytest.fixture
def create_employee() -> Employee:
    factory = EmployeeFactory.create()
    return factory


@pytest.fixture
def api_client():
    client = APIClient()
    return client
