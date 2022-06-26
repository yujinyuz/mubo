from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from mubo.apps.users.models import User

# Register your models here.


class MyUserAdmin(UserAdmin):
    model = User


admin.site.register(User, MyUserAdmin)
