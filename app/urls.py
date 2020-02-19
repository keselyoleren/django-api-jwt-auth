
from django.contrib import admin
from django.urls import path, include
from api.serialize import LoginApiView, RegisterApiView, ListUserApiiew
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/register/", RegisterApiView.as_view(), name="register"),
    path("api/login/", LoginApiView.as_view(), name="login"),
    path("api/list-user", ListUserApiiew.as_view(), name="list-user")
]
