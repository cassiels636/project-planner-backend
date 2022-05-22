from rest_framework.routers import SimpleRouter
from core.user.viewsets import UserViewSet
from core.auth.viewsets import LoginViewSet, RegisterViewSet, RefreshViewSet

routes = SimpleRouter()

# Authentication
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegisterViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# User
routes.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    *routes.urls
]