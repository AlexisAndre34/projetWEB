"""projectWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', views.homepage, name='homepage'),
    path('login/',views.login_in, name='login'),
    path('logout/', views.logout_acc, name='logout'),
    path('signup/', views.sign_up, name='signup'),
    path('account/profil/', views.read_myaccount, name='my_account'),
    path('account/update/', views.update_account, name='update_account'),
    path('group/create/', views.create_group, name="create_group"),
    path('group/list/members/<int:idG>/',views.list_member,name="list_member"), #LIST des membres a supprimer peut etre
    path('group/list/<int:idG>', views.list_groups, name="list_groups"),
    path('group/list_my_groups/<int:id>', views.group_by_user, name="list_group_by_user"),
    path('group/read/<int:idG>/<int:idP>', views.read_group, name="read_group"),
    path('group/update/<int:idG>', views.update_group, name="update_group"),
    path('group/delete/<int:idG>', views.delete_group, name='delete_group'),
    path('publication/create/<int:idG>', views.create_publication, name="create_publication")
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

