from django.shortcuts import render, redirect, get_object_or_404
from .models import Employe
from .forms import EmployeForm


# Create your views here.


def list_employes(request):
    employes = Employe.objects.all()
    return render(request, "employe/list.html", {"employes": employes})


def add_employe(request):
    form = EmployeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("list_employes")
    return render(request, "employe/form.html", {"form": form})


def edit_employe(request, employe_id):
    employe = get_object_or_404(Employe, id=employe_id)
    form = EmployeForm(request.POST or None, instance=employe)
    if form.is_valid():
        form.save()
        return redirect("list_employes")
    return render(request, "employe/form.html", {"form": form, "employe": employe})


def delete_employe(request, employe_id):
    employe = get_object_or_404(Employe, id=employe_id)
    if request.method == "POST":
        employe.delete()
        return redirect("list_employes")
    return render(request, "employe/confirm_delete.html", {"employe": employe})
