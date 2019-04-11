from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
from django.views.generic import TemplateView

pre = settings.NGINX_PRE

urlpatterns = [
    url(r'^'+pre+'$', RedirectView.as_view(url=settings.STATIC_URL + "/index.html")),
    url(r'^'+pre+'api/', include('api.urls')),
    url(r'^'+pre+'admin/', admin.site.urls),
    url(pre+'api-auth/', include('rest_framework.urls')),

    #url(r'^docs/', include('rest_framework_docs.urls')),
]