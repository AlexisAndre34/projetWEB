from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('account/update', views.update_account, name='update_account'),
    path('group/create/<int:idAcc>', views.create_group, name="create_group"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
