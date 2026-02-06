from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.http import HttpResponse
from cbvapp.models import company

# Create your views here.
# class Myclass(View):
#     def get(self,request):

#         return HttpResponse("This is class Based view")

class Myclass(TemplateView):
    template_name = "index.html"

class Allcompanylist(ListView):
    model = company
    template_name = "company_list.html"

class CompanyDetails(DetailView):
    model = company
    context_object_name = "company_details"
    template_name = "company_details.html"

class AddNewCompany(CreateView):
    model = company
    fields = "__all__"
    template_name = "company_form.html"

class CompanyUpdate(UpdateView):
    model = company
    fields = ["name","ceo"]
    template_name = "company_form.html"
