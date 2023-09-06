import pytest
from http import HTTPStatus
from django.contrib.auth.models import User
from genericview.constants import SKILL_NAME, SKILL_LIST_CREATE_URL, SKILL_UPDATE_NAME, EMPLOYEE_NAME, \
    EMPLOYEE_CREATE_URL, EMPLOYEE_LIST_URL, EMPLOYEE_UPDATE_NAME, EMPLOYEE_UPDATE_URL, \
    EMPLOYEE_DELETE_URL, EMPLOYEE_DETAIL_URL
from genericview.models import Skill, Employee

pytestmark = pytest.mark.django_db


class TestSkillAPI:

    def test_skill_create(self, api_client):
        data = {
            'name': SKILL_NAME
        }
        user = User.objects.create_user(username='pakshal', password='1234')
        api_client.force_authenticate(user)
        response = api_client.post(SKILL_LIST_CREATE_URL, data, format='json')
        assert response.status_code == HTTPStatus.CREATED
        assert Skill.objects.filter(name=SKILL_NAME).exists()

    def test_skill_list(self, create_skill, api_client):
        user = User.objects.create_user(username='pakshal', password='1234')
        api_client.force_authenticate(user)
        response = api_client.get(SKILL_LIST_CREATE_URL)
        assert response.status_code == HTTPStatus.OK
        assert len(response.data) == 1

    def test_skill_update(self, create_skill, api_client):
        user = User.objects.create_user(username='pakshal', password='1234')
        api_client.force_authenticate(user)
        data = {
            'name': SKILL_UPDATE_NAME
        }
        response = api_client.put(f"{SKILL_LIST_CREATE_URL}{create_skill.pk}/", data=data, format='json')
        create_skill.refresh_from_db()
        assert response.status_code == HTTPStatus.OK
        assert create_skill.name == SKILL_UPDATE_NAME
        assert Skill.objects.filter(name=SKILL_UPDATE_NAME).exists()

    def test_skill_delete(self, create_skill, api_client):
        user = User.objects.create_user(username='pakshal', password='1234')
        api_client.force_authenticate(user)
        response = api_client.delete(f"{SKILL_LIST_CREATE_URL}{create_skill.pk}/")
        assert response.status_code == HTTPStatus.NO_CONTENT
        assert not Skill.objects.filter(id=create_skill.pk).exists()

    def test_skill_detail(self, create_skill, api_client):
        user = User.objects.create_user(username='pakshal', password='1234')
        api_client.force_authenticate(user)
        response = api_client.get(f"{SKILL_LIST_CREATE_URL}{create_skill.pk}/")
        assert response.status_code == HTTPStatus.OK
        assert response.data['name'] == create_skill.name


class TestEmployeeAPI:

    def test_employee_create(self, create_skill, api_client):
        data = {
            'name': EMPLOYEE_NAME,
            'skill': create_skill.pk
        }
        user = User.objects.create_user(username='pakshal', password='1234')
        api_client.force_authenticate(user)
        response = api_client.post(EMPLOYEE_CREATE_URL, data, format='json')
        assert response.status_code == HTTPStatus.CREATED
        assert Employee.objects.filter(name=EMPLOYEE_NAME).exists()

    def test_employee_list(self, create_employee, api_client):
        user = User.objects.create_user(username='pakshal', password='1234')
        api_client.force_authenticate(user)
        response = api_client.get(EMPLOYEE_LIST_URL)
        assert response.status_code == HTTPStatus.OK
        assert len(response.data) == 1

    def test_employee_update(self, create_skill, create_employee, api_client):
        user = User.objects.create_user(username='pakshal', password='1234')
        api_client.force_authenticate(user)
        data = {
            'name': EMPLOYEE_UPDATE_NAME,
            'skill': create_skill.pk
        }
        response = api_client.put(f"{EMPLOYEE_UPDATE_URL}{create_employee.pk}/", data, format='json')
        create_employee.refresh_from_db()
        assert response.status_code == HTTPStatus.OK
        assert create_employee.name == EMPLOYEE_UPDATE_NAME
        assert Employee.objects.filter(name=EMPLOYEE_UPDATE_NAME).exists()

    def test_employee_delete(self, create_employee, api_client):
        user = User.objects.create_user(username='pakshal', password='1234')
        api_client.force_authenticate(user)
        response = api_client.delete(f"{EMPLOYEE_DELETE_URL}{create_employee.pk}/")
        assert response.status_code == HTTPStatus.NO_CONTENT
        assert not Employee.objects.filter(id=create_employee.pk).exists()

    def test_employee_detail(self, create_employee, api_client):
        user = User.objects.create_user(username='pakshal', password='1234')
        api_client.force_authenticate(user)
        response = api_client.get(f"{EMPLOYEE_DETAIL_URL}{create_employee.pk}/")
        assert response.status_code == HTTPStatus.OK
        assert response.data['name'] == create_employee.name
