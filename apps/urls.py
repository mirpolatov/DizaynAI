from rest_framework.routers import DefaultRouter
from django.urls import path, include

from apps.views import RegisterView, SiteModelView, LogoModelView, ProfileModelView, MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router2 = DefaultRouter()
router3 = DefaultRouter()
router4 = DefaultRouter()

router.register('register', RegisterView, basename='register')
router2.register('site', SiteModelView, basename='site')
router3.register('logo', LogoModelView, basename='logo')
router4.register('profile', ProfileModelView, basename='profile')

urlpatterns = [
    path('register/', include(router.urls)),
    path('site/', include(router2.urls)),
    path('logo/', include(router3.urls)),
    path('profile/', include(router4.urls)),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

]
