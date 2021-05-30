from rest_framework import viewsets, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Note
from .permissions import IsOwner
from .serializers import NoteSerializer


# class NoteViewSet(viewsets.ModelViewSet):
#     queryset = Note.objects.all().order_by('create_at')
#     serializer_class = NoteSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         return Note.objects.filter(author=self.request.user)
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)


class NoteListAPIView(ListCreateAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all().order_by('create_at')
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NoteDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all().order_by('create_at')
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    lookup_field = 'id'

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
