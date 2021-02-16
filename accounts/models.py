from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE
from PIL import Image


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    is_staff = models.BooleanField(default=False, null=True)
    is_superuser = models.BooleanField(default=False, null=True)
    is_active = models.BooleanField(default=True, null=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_email(self):
        return self.email

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()


class Category(models.Model):
    category_name = models.CharField(max_length=225, null=True, blank=True)
    category_code = models.CharField(max_length=225, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.category_name


class Product(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    product_name = models.CharField(max_length=225, null=True, blank=True)
    product_code = models.CharField(max_length=225, null=True, blank=True)
    product_images = models.ImageField(default='default_product.png', upload_to='product_img', null=True, blank=True)
    product_mfg_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def save(self,*args, **kwargs):
        super(Product, self).save(*args, **kwargs)

        img = Image.open(self.product_images.path)
        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.product_images.path)

    def __str__(self):
        return self.product_name