from django.urls import path
from cbvapp import views

urlpatterns = [
    path('', views.Allcompanylist.as_view(), name='list'),
    path('<int:pk>/', views.CompanyDetails.as_view(), name='detail'),
]