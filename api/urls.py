from django.urls import path
from .views import ItemList, ItemDetail, LocationList, LocationDetail

urlpatterns = [
    path('items/', ItemList.as_view()),
    path('items/<int:pk>/', ItemDetail.as_view()),
    path('locations/', LocationList.as_view()),
    path('locations/<int:pk>/', LocationDetail.as_view()),
]