from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('printorders/', views.printorder_list, name='printorder_list'),
    path('printorders/create/', views.printorder_create, name='printorder_create'),
    path('printorders/<int:pk>/edit/', views.printorder_edit, name='printorder_edit'),
    path('printorders/<int:pk>/delete/', views.printorder_delete, name='printorder_delete'),
    path('printproducts/', views.printproduct_list, name='printproduct_list'),
    path('printproducts/create/', views.printproduct_create, name='printproduct_create'),
    path('printproducts/<int:pk>/edit/', views.printproduct_edit, name='printproduct_edit'),
    path('printproducts/<int:pk>/delete/', views.printproduct_delete, name='printproduct_delete'),
    path('printcustomers/', views.printcustomer_list, name='printcustomer_list'),
    path('printcustomers/create/', views.printcustomer_create, name='printcustomer_create'),
    path('printcustomers/<int:pk>/edit/', views.printcustomer_edit, name='printcustomer_edit'),
    path('printcustomers/<int:pk>/delete/', views.printcustomer_delete, name='printcustomer_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
