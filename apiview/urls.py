from django.urls import path
from apiview.views import AuthorView, BookView

app_name = 'apiview'

urlpatterns = [

    path('authors/', AuthorView.as_view()),
    path('authors/<int:pk>/', AuthorView.as_view()),

    path('books/', BookView.as_view()),
    path('books/<int:pk>/', BookView.as_view())

]
