from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('backend.core.customers.urls')),
    path('auth/', include('backend.core.urls')),
    path('', include('backend.core.urls')),  # Troque 'nome_do_app' pelo nome do seu app

]