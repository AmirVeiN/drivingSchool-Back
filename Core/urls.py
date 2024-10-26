from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/admin/', include("Admin.urls")),
    # path('api/v1/user/', include("User.urls")),
]
