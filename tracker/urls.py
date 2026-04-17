from django.urls import path
from.import views

urlpatterns = [
    path('',views.home, name='home'),
    path('add/',views.add_expense, name='add'),
    path('delete/<int:id>/',views.delete_expense, name='delete'),
    path('edit/<int:id>/',views.edit_expense, name='edit'),
    path('signup/',views.signup, name='signup'),


]