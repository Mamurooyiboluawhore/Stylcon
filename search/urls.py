from django.urls import include, path
from .views import SearchView


urlpatterns = [
    # ex: /polls/
    path('', SearchView.as_view(), name='search'),
    
]