from rest_framework.routers import DefaultRouter

from restaurant.views import BookingViewSet, MenuViewSet, UserViewSet

router = DefaultRouter()
router.register(r'booking', BookingViewSet, basename='booking')
router.register(r'menu', MenuViewSet, basename='menu')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = router.urls
