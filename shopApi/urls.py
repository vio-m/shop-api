from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from fashionStore import views
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)


urlpatterns = [
	path('', include(router.urls)),
    path('admin/', admin.site.urls),
	path('api/', include('fashionStore.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)