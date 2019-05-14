from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('account/update/', views.update_account, name='update_account'),
    path('group/create/', views.create_group, name="create_group"),
    path('group/list/', views.group_by_user, name="list_group_by_user"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
