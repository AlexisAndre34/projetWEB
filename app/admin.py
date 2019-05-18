from django.contrib import admin
from .models import Account, Publication, Comment, Group, Belong, Join
# Register your models here.

admin.site.register(Account)
admin.site.register(Publication)
admin.site.register(Comment)
admin.site.register(Group)
admin.site.register(Belong)
admin.site.register(Join)