from django.urls import include, path
from .views import CatalogueAPIViews



urlpatterns = [
    path('', CatalogueAPIViews.as_view(), name='catalogue-list'),
    path('create-catalgue/', CatalogueAPIViews.as_view(), name='create-catalogue'),
    path('<uuid:catalogue_id>/update/', CatalogueAPIViews.as_view(), name='product_review_detail'),
    path('<uuid:catalogue_id>/delete', CatalogueAPIViews.as_view(), name='product_review_delete'),
]