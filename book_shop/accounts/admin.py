from django.contrib import admin
from .models import CustomUser, Comment, Award, Order, Library

admin.site.register(CustomUser)
admin.site.register(Comment)
admin.site.register(Award)
admin.site.register(Order)
admin.site.register(Library)
