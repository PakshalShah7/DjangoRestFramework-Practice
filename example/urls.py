from django.urls import path
from example.views import artist_list, artist_detail

app_name = 'example'

urlpatterns = [

    path('artists/', artist_list),
    path('artists/<int:pk>/', artist_detail)

]
