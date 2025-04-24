from django.urls import path, include
from .views import RegisterView, Login, PostView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'postview',PostView, basename='postview' )

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view() , name='register'),
    path('login/', Login.as_view(), name= 'login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]