from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category', CategoryCreateView.as_view(), name='category'),
    path('category-update/<str:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('category-details/<str:pk>', CategoryDetailView.as_view(), name='category_details'),

    path('product', ProductCreateView.as_view(), name='product'),
    path('product-details/<str:pk>', ProductDetailView.as_view(), name='product_details'),
    path('product-update/<str:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product-delete/<str:pk>', DeleteProduct, name='product_delete'),

    path('register', RegistrationView, name='register'),
    path('login', login_view, name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='home.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)