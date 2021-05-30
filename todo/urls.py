from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet

router = DefaultRouter()
router.register('', NoteViewSet, basename='todos')
urlpatterns = router.urls