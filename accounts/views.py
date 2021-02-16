from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, UpdateView, View, ListView, DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from django.contrib import messages
from datetime import date
from .forms import *
from .decorators import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class Home(ListView):
    model = Category
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)


        categories = Category.objects.all()


        context['categories'] = categories
        products = Product.objects.all()
        context['products'] = products

        return context


@unauthenticated_user
def RegistrationView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('sucess')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


@unauthenticated_user
def login_view(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password is incorrect')
    return render(request, 'login.html')


@method_decorator(login_required, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category.html'

    def form_valid(self, form):
        form.save()
        return redirect('home')


@method_decorator(login_required, name='dispatch')
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category-details.html'

    def get_context_data(self,*args ,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        category_details = Category.objects.get(id=self.kwargs['pk'])
        context['category_details'] = category_details
        return context


@method_decorator(login_required, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category.html'

    def form_valid(self, form):
        form.instance.updated_at = date.today()
        form.save()
        return redirect('home')


@method_decorator(login_required, name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product.html'

    def form_valid(self, form):
        form.save()
        return redirect('home')


@method_decorator(login_required, name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product-details.html'

    def get_context_data(self,*args ,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        product_details = Product.objects.get(id=self.kwargs['pk'])
        context['product_details'] = product_details
        return context


@method_decorator(login_required, name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product.html'

    def form_valid(self, form):
        form.save()
        return redirect('home')


@login_required
def DeleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    context = {'product':product}
    return render(request, 'product_delete.html', context)