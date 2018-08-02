from django.conf.urls import url
from .views import FeedbackFormView

from rest_framework import routers
from .views import FeedbackViewSet

# Создаем router и регистрируем наш ViewSet
router = routers.DefaultRouter()
router.register(r'feedback', FeedbackViewSet)

# URLs настраиваются автоматически роутером
urlpatterns = router.urls
