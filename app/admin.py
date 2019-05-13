from django.contrib import admin
from .models import Account, Category, Publication, Comment, Group, File, Belong
# Register your models here.

admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Publication)
admin.site.register(Comment)
admin.site.register(Group)
admin.site.register(File)
admin.site.register(Belong)