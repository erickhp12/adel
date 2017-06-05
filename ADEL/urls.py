from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from ADEL import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include("empleados.urls")),
    url(r'^', include("pacientes.urls")),
    url(r'^', include("login.urls")),
    url(r'^', include("visitas.urls")),
    url(r'^', include("proveedores.urls")),

] + static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
