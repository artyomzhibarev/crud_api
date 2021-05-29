from django.urls import path
from rest_framework import routers
from .views import UserViewSet, NoteViewSet

router = routers.SimpleRouter()
router.register(r'todos', NoteViewSet, basename='notes')
router.register(r'users', UserViewSet, basename='users')
urlpatterns = router.urls

# urlpatterns += [
#     path('about/', views.AboutView.as_view(), name='about'),
#                 ]
