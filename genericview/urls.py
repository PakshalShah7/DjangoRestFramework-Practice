from django.urls import path
from genericview.views import SkillListCreateView, SkillRetrieveUpdateDestroyView, EmployeeCreateView, \
    EmployeeListView, EmployeeUpdateView, EmployeeDeleteView, EmployeeDetailView, EmployeeDetailUpdateView, \
    EmployeeDetailDeleteView

app_name = 'genericview'

urlpatterns = [

    path('skills/', SkillListCreateView.as_view(), name='skill_list_create'),
    path('skills/<int:pk>/', SkillRetrieveUpdateDestroyView.as_view(), name='skill_detail_update_delete'),

    path('employee-create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employee-update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee-delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee_delete'),
    path('employee-detail/<int:pk>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('employee-detail-update/<int:pk>/', EmployeeDetailUpdateView.as_view(), name='employee_detail_update'),
    path('employee-detail-delete/<int:pk>/', EmployeeDetailDeleteView.as_view(), name='employee_detail_delete'),

]
