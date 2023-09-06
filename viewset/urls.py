from django.urls import path, include
from rest_framework.routers import SimpleRouter
from viewset.views import UserView
from rest_framework.authtoken import views

app_name = 'viewset'

router = SimpleRouter()
router.register(r'users', UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token)
]

urlpatterns += router.urls
