import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, force_authenticate
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory

from todo.models import Note
from todo.serializers import NoteSerializer
from todo.views import NoteListAPIView


class NoteApiTestCase(APITestCase):

    def test_create_and_get_note(self):
        factory = APIRequestFactory()
        test_user = User.objects.create_user(
            username='jacob', email='jacob@gmail.com', password='top_s324ecrweret')
        view = NoteListAPIView.as_view()
        Note.objects.create(author=test_user, title='Test', text='Test')
        Note.objects.create(author=test_user, title='Test2', text='Test2')
        request = factory.get(f'http://127.0.0.1:8000/todos/{test_user.username}/')
        force_authenticate(request, user=test_user)
        response = view(request)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_notes(self):
        factory = APIRequestFactory()
        test_user = User.objects.create_user(
            username='jacob', email='jacob@gmail.com', password='top_s324ecrweret')
        view = NoteListAPIView.as_view()
        note1 = Note.objects.create(author=test_user, title='Test', text='Test')
        request = factory.get(f'http://127.0.0.1:8000/todos/{test_user.username}/')
        force_authenticate(request, user=test_user)
        response = view(request)
        serializer_data = NoteSerializer(note1).data
        self.assertEqual(serializer_data, response.data)

    def test_create_note_auth_user(self):
        factory = APIRequestFactory()
        test_user = User.objects.create_user(
            username='jacob', email='jacob@gmail.com', password='top_s324ecrweret')
        view = NoteListAPIView.as_view()
        request = factory.post(f'http://127.0.0.1:8000/todos/{test_user.username}/',
                               {
                                   'title': 'new idea',
                                   'text': 'Test',
                                   'author': test_user
                               }
                               )
        force_authenticate(request, user=test_user)
        response = view(request)
        print(response.data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)


