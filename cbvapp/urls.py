from django.urls import path
from cbvapp import views

urlpatterns = [
    path('', views.Allcompanylist.as_view(), name='list'),
    path('<int:pk>/', views.CompanyDetails.as_view(), name='details'),
    path('edit/<int:pk>/', views.CompanyUpdate.as_view(), name='edit'),
    path('create/', views.AddNewCompany.as_view(), name='create'),
    path('delete/<int:pk>/', views.DeleteCompany.as_view(), name='delete'),
    path('emi/<int:id>/', views.EmiCalculatorView, name='emi'),
    path('product/<int:pk>/', views.ProductDetails.as_view(), name='products_detail'),

]