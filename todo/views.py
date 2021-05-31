from rest_framework import viewsets, permissions, mixins, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet

from .models import Note
from .permissions import IsOwner
from .serializers import NoteSerializer


# class NoteViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Note.objects.all().order_by('create_at')
#     serializer_class = NoteSerializer
#     permission_classes = [permissions.IsAuthenticated, IsOwner]
#     lookup_field = 'id'
#     slug_field = 'username'
#
#     def get_queryset(self):
#         return Note.objects.filter(author=self.request.user)
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)
#
#     def get_username(self):
#         user = self.request.user
#         return user.username


# class NoteList(ReadOnlyModelViewSet):
#     serializer_class = NoteSerializer
#     permission_classes = [permissions.IsAuthenticated, ]
#
#     def get_queryset(self):
#         return Note.objects.filter(author=self.request.user)
#
#
# class NoteDetail(mixins.CreateModelMixin,
#                  mixins.RetrieveModelMixin,
#                  mixins.UpdateModelMixin,
#                  mixins.DestroyModelMixin,
#                  GenericViewSet):
#     serializer_class = NoteSerializer
#     queryset = Note.objects.all().order_by('create_at')
#     permission_classes = (permissions.IsAuthenticated, IsOwner)
#     lookup_field = 'id'
#
#     def get_queryset(self):
#         return Note.objects.filter(author=self.request.user)
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)


class NoteListAPIView(ListCreateAPIView):
    # queryset = Note.objects.all().order_by('create_at')
    serializer_class = NoteSerializer
    # permission_classes = (permissions.IsAuthenticated, )
    permission_classes = (IsOwner,)

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user).order_by('-create_at')

    def perform_create(self, serializer):
        serializer.validated_data['author'] = self.request.user
        serializer.save()

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if request.user.is_authenticated:
            notes = self.get_serializer(queryset, many=True)
            return Response(notes.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class NoteDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    # permission_classes = (permissions.IsAuthenticated, )
    queryset = Note.objects.all().order_by('create_at')
    permission_classes = (IsOwner,)
    lookup_field = "id"

    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        if not request.user.is_authenticated:
            return Response(serializer.data, status=status.HTTP_403_FORBIDDEN)
        else:
            return super().retrieve(request, *args, **kwargs)