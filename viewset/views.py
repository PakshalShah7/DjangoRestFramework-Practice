from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from viewset.pagination import CustomPageNumberPagination
from viewset.serializers import UserSerializer


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['username']
    pagination_class = CustomPageNumberPagination
