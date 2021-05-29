from rest_framework import viewsets, permissions

from todo.models import CustomUser, Note
from todo.serializers import UserSerializer, NoteSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('create_at')
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
