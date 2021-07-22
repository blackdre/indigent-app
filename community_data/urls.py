from django.urls import path
from .views import PersonList, PersonDetail, ResidenceList, ResidenceDetail

urlpatterns = [
    path('<int:pk>/', PersonDetail.as_view()),
    path('', PersonList.as_view()),
    path('house/<int:pk>/', ResidenceDetail.as_view()),
    path('house/', ResidenceList.as_view()),
]
