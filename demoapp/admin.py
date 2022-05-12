from django.contrib import admin
from .models import DemoUser
# Register your models here.
@admin.register(DemoUser)
class DemoUserModelAdmin(admin.ModelAdmin):
    list_display = [
        'id','fname','lname','username','email','role','pass1','city','state','pin','profile_img'
    ]