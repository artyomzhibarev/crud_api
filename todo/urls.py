from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.views.decorators.csrf import csrf_exempt

# router = DefaultRouter()
# router.register(r'notes', views.NoteList, basename='notes')
# router.register(r'note', views.NoteDetail, basename='note')
# urlpatterns = router.urls

urlpatterns = [
    path(r'<username>/', csrf_exempt(views.NoteListAPIView.as_view()), name='notes'),
    path(r'<username>/<int:pk>/', csrf_exempt(views.NoteDetailAPIView.as_view()), name='note')
]

urlpatterns += [
    path(r'<username>/<int:pk>/', csrf_exempt(views.NoteDetailAPIView.as_view()), name='note_for_tests')
]
