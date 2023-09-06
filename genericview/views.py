from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, \
    ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, RetrieveUpdateAPIView, \
    RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from genericview.models import Skill, Employee
from genericview.serializers import SkillSerializer, EmployeeSerializer


class SkillListCreateView(ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class SkillRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class EmployeeCreateView(CreateAPIView):
    serializer_class = EmployeeSerializer


class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeUpdateView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDeleteView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailUpdateView(RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailDeleteView(RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
