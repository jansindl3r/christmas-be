from django.contrib import admin
from christmas.models import Group, User, Wish, Comment

# Register your models here.
admin.site.register(Group)
admin.site.register(User)
admin.site.register(Wish)
admin.site.register(Comment)