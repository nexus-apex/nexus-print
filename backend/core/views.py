import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import PrintOrder, PrintProduct, PrintCustomer


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['printorder_count'] = PrintOrder.objects.count()
    ctx['printorder_business_cards'] = PrintOrder.objects.filter(product_type='business_cards').count()
    ctx['printorder_banners'] = PrintOrder.objects.filter(product_type='banners').count()
    ctx['printorder_brochures'] = PrintOrder.objects.filter(product_type='brochures').count()
    ctx['printorder_total_total'] = PrintOrder.objects.aggregate(t=Sum('total'))['t'] or 0
    ctx['printproduct_count'] = PrintProduct.objects.count()
    ctx['printproduct_cards'] = PrintProduct.objects.filter(category='cards').count()
    ctx['printproduct_large_format'] = PrintProduct.objects.filter(category='large_format').count()
    ctx['printproduct_marketing'] = PrintProduct.objects.filter(category='marketing').count()
    ctx['printproduct_total_base_price'] = PrintProduct.objects.aggregate(t=Sum('base_price'))['t'] or 0
    ctx['printcustomer_count'] = PrintCustomer.objects.count()
    ctx['printcustomer_active'] = PrintCustomer.objects.filter(status='active').count()
    ctx['printcustomer_inactive'] = PrintCustomer.objects.filter(status='inactive').count()
    ctx['printcustomer_total_total_spent'] = PrintCustomer.objects.aggregate(t=Sum('total_spent'))['t'] or 0
    ctx['recent'] = PrintOrder.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def printorder_list(request):
    qs = PrintOrder.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(order_number__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(product_type=status_filter)
    return render(request, 'printorder_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def printorder_create(request):
    if request.method == 'POST':
        obj = PrintOrder()
        obj.order_number = request.POST.get('order_number', '')
        obj.customer_name = request.POST.get('customer_name', '')
        obj.product_type = request.POST.get('product_type', '')
        obj.quantity = request.POST.get('quantity') or 0
        obj.total = request.POST.get('total') or 0
        obj.status = request.POST.get('status', '')
        obj.due_date = request.POST.get('due_date') or None
        obj.save()
        return redirect('/printorders/')
    return render(request, 'printorder_form.html', {'editing': False})


@login_required
def printorder_edit(request, pk):
    obj = get_object_or_404(PrintOrder, pk=pk)
    if request.method == 'POST':
        obj.order_number = request.POST.get('order_number', '')
        obj.customer_name = request.POST.get('customer_name', '')
        obj.product_type = request.POST.get('product_type', '')
        obj.quantity = request.POST.get('quantity') or 0
        obj.total = request.POST.get('total') or 0
        obj.status = request.POST.get('status', '')
        obj.due_date = request.POST.get('due_date') or None
        obj.save()
        return redirect('/printorders/')
    return render(request, 'printorder_form.html', {'record': obj, 'editing': True})


@login_required
def printorder_delete(request, pk):
    obj = get_object_or_404(PrintOrder, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/printorders/')


@login_required
def printproduct_list(request):
    qs = PrintProduct.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(category=status_filter)
    return render(request, 'printproduct_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def printproduct_create(request):
    if request.method == 'POST':
        obj = PrintProduct()
        obj.name = request.POST.get('name', '')
        obj.category = request.POST.get('category', '')
        obj.base_price = request.POST.get('base_price') or 0
        obj.min_quantity = request.POST.get('min_quantity') or 0
        obj.production_time_days = request.POST.get('production_time_days') or 0
        obj.status = request.POST.get('status', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/printproducts/')
    return render(request, 'printproduct_form.html', {'editing': False})


@login_required
def printproduct_edit(request, pk):
    obj = get_object_or_404(PrintProduct, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.category = request.POST.get('category', '')
        obj.base_price = request.POST.get('base_price') or 0
        obj.min_quantity = request.POST.get('min_quantity') or 0
        obj.production_time_days = request.POST.get('production_time_days') or 0
        obj.status = request.POST.get('status', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/printproducts/')
    return render(request, 'printproduct_form.html', {'record': obj, 'editing': True})


@login_required
def printproduct_delete(request, pk):
    obj = get_object_or_404(PrintProduct, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/printproducts/')


@login_required
def printcustomer_list(request):
    qs = PrintCustomer.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'printcustomer_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def printcustomer_create(request):
    if request.method == 'POST':
        obj = PrintCustomer()
        obj.name = request.POST.get('name', '')
        obj.company = request.POST.get('company', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.orders_count = request.POST.get('orders_count') or 0
        obj.total_spent = request.POST.get('total_spent') or 0
        obj.status = request.POST.get('status', '')
        obj.discount_rate = request.POST.get('discount_rate') or 0
        obj.save()
        return redirect('/printcustomers/')
    return render(request, 'printcustomer_form.html', {'editing': False})


@login_required
def printcustomer_edit(request, pk):
    obj = get_object_or_404(PrintCustomer, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.company = request.POST.get('company', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.orders_count = request.POST.get('orders_count') or 0
        obj.total_spent = request.POST.get('total_spent') or 0
        obj.status = request.POST.get('status', '')
        obj.discount_rate = request.POST.get('discount_rate') or 0
        obj.save()
        return redirect('/printcustomers/')
    return render(request, 'printcustomer_form.html', {'record': obj, 'editing': True})


@login_required
def printcustomer_delete(request, pk):
    obj = get_object_or_404(PrintCustomer, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/printcustomers/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['printorder_count'] = PrintOrder.objects.count()
    data['printproduct_count'] = PrintProduct.objects.count()
    data['printcustomer_count'] = PrintCustomer.objects.count()
    return JsonResponse(data)
