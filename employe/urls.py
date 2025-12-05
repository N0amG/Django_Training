from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_employes, name="list_employes"),
    path("add/", views.add_employe, name="add_employe"),
    path("modify/<int:employe_id>/", views.edit_employe, name="edit_employe"),
    path("delete/<int:employe_id>/", views.delete_employe, name="delete_employe"),
    path("confirm_delete/<int:employe_id>/", views.delete_employe, name="confirm_delete_employe"),
]
