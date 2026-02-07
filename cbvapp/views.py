from django.shortcuts import render
from django.urls import reverse_lazy
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

class DeleteCompany(DeleteView):
    model = company
    template_name = "company_confirm_delete.html"
    # success_url = "/company"
    success_url = reverse_lazy("list")

from cbvapp.forms import EMIForm
from cbvapp.models import product


def EmiCalculatorView(request,id=0):
    prod = product.objects.get(id=id)
    initial = {"prod_name": prod.prod_name, "price": prod.price, "loan_amount": prod.price}
    results = None

    if request.method == "POST":
        form = EMIForm(request.POST, initial=initial)
        if form.is_valid():
            loan = form.cleaned_data["loan_amount"]
            years = int(form.cleaned_data["tenures"])
            annual_rate = float(form.cleaned_data["annual_rate"])

            P = float(loan)
            monthly_r = annual_rate / 12.0 / 100.0
            n = years * 12
            if monthly_r == 0:
                emi = P / n
            else:
                r = monthly_r
                emi = P * r * (1 + r) ** n / ((1 + r) ** n - 1)
            results = [{"years": years, "months": n, "emi": round(emi, 2)}]
    else:
        form = EMIForm(initial=initial)

    return render(request, "emi_calculator.html", {"form": form, "product": prod, "results": results})