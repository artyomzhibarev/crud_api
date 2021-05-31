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
    def setUp(self) -> None:
        self.test_user = User.objects.create_user(
            username='jacob', email='jacob@gmail.com', password='top_s324ecrweret')
        self.note1 = Note.objects.create(author=self.test_user, title='Test', text='Test')
        self.note2 = Note.objects.create(author=self.test_user, title='Test2', text='Test2')
        self.note3 = Note.objects.create(author=self.test_user, title='Test3', text='Test3')
        self.view = NoteListAPIView.as_view()
        self.factory = APIRequestFactory()

    def test_get_notes(self):
        """
        Retrieving authenticated user notes
        1. Сравнение желаемого статуса ответа от сервера с полученным
        2. Сравнение сериализованных данных с полученными данными в ответе
        3. Количество созданных заметок должно соответствовать фактическому количеству создаваемых заметок
        :return:
        """
        request = self.factory.get(f'http://127.0.0.1:8000/todos/{self.test_user.username}/')
        force_authenticate(request, user=self.test_user)
        response = self.view(request)
        serializer_data = NoteSerializer([self.note3, self.note2, self.note1], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(3, len(serializer_data))

    # def test_create_and_get_note(self):
    #     factory = APIRequestFactory()
    #     test_user = User.objects.create_user(
    #         username='jacob', email='jacob@gmail.com', password='top_s324ecrweret')
    #     view = NoteListAPIView.as_view()
    #     Note.objects.create(author=test_user, title='Test', text='Test')
    #     Note.objects.create(author=test_user, title='Test2', text='Test2')
    #     request = factory.get(f'http://127.0.0.1:8000/todos/{test_user.username}/')
    #     force_authenticate(request, user=test_user)
    #     response = view(request)
    #     self.assertEqual(status.HTTP_200_OK, response.status_code)

    # def test_create_note(self):
    #     factory = APIRequestFactory()
    #     # test_user = User.objects.create_user(
    #     #     username='jacob', email='jacob@gmail.com', password='top_s324ecrweret')
    #     data = {
    #         'author': f'{test_user}',
    #         'title': 'Test',
    #         'text': 'Test'
    #     }
    #     # json_data = json.dumps(data)
    #     # view = NoteListAPIView.as_view()
    #     # request = factory.post(f'http://127.0.0.1:8000/todos/{test_user.username}/')
    #     # self.client.force_login(test_user)
    #     # force_authenticate(request, user=test_user)
    #     # response = view(request)
    #     # print(response)
    #     # self.assertEqual(status.HTTP_200_OK, response.status_code)

    # def test_create_note_auth_user(self):
    #     factory = APIRequestFactory()
    #     test_user = User.objects.create_user(
    #         username='jacob', email='jacob@gmail.com', password='top_s324ecrweret')
    #     view = NoteListAPIView.as_view()
    #     request = factory.post(f'http://127.0.0.1:8000/todos/{test_user.username}/',
    #                            {
    #                                'title': 'new idea',
    #                                'text': 'Test',
    #                                'author': test_user
    #                            }
    #                            )
    #     force_authenticate(request, user=test_user)
    #     response = view(request)
    #     print(response.data)
    #     self.assertEqual(status.HTTP_201_CREATED, response.status_code)
