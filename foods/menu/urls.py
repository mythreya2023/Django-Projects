from django.urls import path
from . import views

urlpatterns = [
    path('', views.allFoods,name="allfoodpage"),
    path('addfood', views.food,name="foodpage"),
    path('editfood',views.edit,name="editpage"),
    path('notes',views.allnotes,name="notespag"),
    path('notes/<int:id>',views.notes,name="notespage"),
    path('notesUpd',views.notesUpd,name="nupdpage"),
]