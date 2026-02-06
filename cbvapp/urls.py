from django.urls import path
from cbvapp import views

urlpatterns = [
    path('', views.Allcompanylist.as_view(), name='list'),
    path('<int:pk>/', views.CompanyDetails.as_view(), name='detail'),
    path('edit/<int:pk>/', views.CompanyUpdate.as_view(), name='edit'),
    path('add/', views.AddNewCompany.as_view(), name='add'),
    path('add/', views.AddNewCompany.as_view(), name='create'),
]