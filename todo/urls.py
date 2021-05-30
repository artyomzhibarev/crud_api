from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register('', views.NoteViewSet, basename='todos')
# urlpatterns = router.urls


urlpatterns = [
    path('<username>/', views.NoteListAPIView.as_view(), name='notes'),
    path('<username>/<int:id>/', views.NoteDetailAPIView.as_view(), name='note')
]
