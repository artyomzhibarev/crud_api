import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, force_authenticate
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory

from todo.models import Note
from todo.serializers import NoteSerializer
from todo.views import NoteListAPIView, NoteDetailAPIView


class NoteApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.test_user = User.objects.create_user(
            username='jacob', email='jacob@gmail.com', password='top_s324ecrweret')
        self.random_user = User.objects.create_user(
            username='random', email='randon@gmail.com', password='random')
        self.note1 = Note.objects.create(author=self.test_user, title='Test', text='Test')
        self.note2 = Note.objects.create(author=self.test_user, title='Test2', text='Test2')
        self.note3 = Note.objects.create(author=self.test_user, title='Test3', text='Test3')
        self.view_set = NoteListAPIView.as_view()
        self.view_detail = NoteDetailAPIView.as_view()
        self.factory = APIRequestFactory()

    def test_get_notes(self):
        """
        1. Сравнение ожидаемого статуса ответа от сервера с полученным
        2. Сравнение сериализованных данных с полученными данными в ответе
        3. Количество созданных заметок должно соответствовать фактическому количеству создаваемых заметок
        :return:
        """
        request = self.factory.get(f'http://127.0.0.1:8000/todos/{self.test_user.username}/')
        force_authenticate(request, user=self.test_user)
        response = self.view_set(request)
        serializer_data = NoteSerializer([self.note3, self.note2, self.note1], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(3, len(serializer_data))

    def test_get_notes_not_authorized_user(self):
        request = self.factory.get(f'http://127.0.0.1:8000/todos/{self.test_user.username}/')
        response = self.view_set(request)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_create_note(self):
        data = {
            'author': f'{self.test_user}',
            'title': 'Test',
            'text': 'Test'
        }
        json_data = json.dumps(data)
        request = self.factory.post(f'http://127.0.0.1:8000/todos/{self.test_user.username}/',
                                    data=json_data, content_type='application/json')
        force_authenticate(request, user=self.test_user)
        response = self.view_set(request, data=json_data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_create_note_not_authorized_user(self):
        data = {
            'author': f'{self.client}',
            'title': 'Test',
            'text': 'Test'
        }
        json_data = json.dumps(data)
        request = self.factory.post(f'http://127.0.0.1:8000/todos/{self.test_user}/',
                                    data=json_data, content_type='application/json')
        response = self.view_set(request, data=json_data)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)

    def test_create_note_with_unsupported_status(self):
        data = {
            'author': f'{self.test_user}',
            'title': 'Test',
            'text': 'Test',
            'status': 'NOT_STATUS'
        }
        json_data = json.dumps(data)
        request = self.factory.post(f'http://127.0.0.1:8000/todos/{self.test_user.username}/',
                                    data=json_data, content_type='application/json')
        force_authenticate(request, user=self.test_user)
        response = self.view_set(request, data=json_data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    # def test_get_note_detail(self):
    #     url = reverse('note_for_tests', kwargs={'pk': self.note3.id})
    #     print(url)
        # request = self.factory.get(url)
        # print(request)
        # force_authenticate(request, user=self.test_user)
        # response = self.view_detail(request)
        # print(response.data)

    # def test_update_note(self):
    #     # note = Note.objects.last()
    #     data = {
    #         'author': f'{self.test_user}',
    #         'title': '1234',
    #         'text': '2424234',
    #         'id': 3,
    #     }
    #     json_data = json.dumps(data)
    #     request = self.factory.put(f'http://127.0.0.1:8000/todos/{self.test_user.username}/{}',
    #                                data=json_data, content_type='application/json')
    #     print(request)
    #     force_authenticate(request, user=self.test_user)
    #     response = self.view_detail(request, data=json_data)
    #     print(response)
    # self.assertEqual(status.HTTP_201_CREATED, response.status_code)
