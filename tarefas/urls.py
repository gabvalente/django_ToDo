from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('create', views.create, name="create"),
    path('save', views.save, name="save"),
    path('update/<int:id>', views.update, name="update"),
    path('save_update/<int:id>', views.save_delete, name="save_update"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('save_delete/<int:id>', views.save_delete, name="save_delete"),

]
