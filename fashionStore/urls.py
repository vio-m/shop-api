from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('product', views.ProductViewSet, basename='product')
router.register('category', views.CategoryViewSet, basename='category')
router.register('brand', views.BrandViewSet, basename='brand')
router.register('order', views.OrderViewSet, basename='order')
router.register('subscription', views.SubscriptionViewSet, basename='subscription')

urlpatterns = [
    path('', include(router.urls)),
    path('category/', views.CategoryViewSet.as_view({'get': 'list'}), name='category'),
    path('brand/', views.BrandViewSet.as_view({'get': 'list'}), name='brand'),
    path('order/', views.OrderViewSet.as_view({'get': 'list'}), name='order'),
    path('subscribe/', views.SubscriptionViewSet.as_view({'get': 'list'}), name='subscription')
]












