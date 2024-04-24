from django.urls import include, path
from .views import SearchView


urlspatterns = [
    # ex: /polls/
    path('', SearchView.as_view(), name='search'),
]