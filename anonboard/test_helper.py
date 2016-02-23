from rest_framework.test import APITestCase, APIClient
from rest_framework      import status

import json


class TestClient(APIClient):
    def _get_japi_http_accept(self, bulk=False):
        return 'application/vnd.api+json'

    def json_get(self, path, data=None, bulk=False, **extra):
        return super(TestClient, self).get(
            path=path,
            data=data,
            follow=True,
            format='json',
            **extra
        )

    def japi_get(self, path, data=None, bulk=False, **extra):
        extra['HTTP_ACCEPT'] = self._get_japi_http_accept(bulk=bulk)

        return self.json_get(path=path, data=data, bulk=bulk, **extra)

    def json_post(self, path, data=None, ext=None, bulk=False, **extra):
        return super(TestClient, self).post(
            path=path,
            data=data,
            follow=True,
            format='json',
            **extra
        )

    def japi_post(self, path, data=None, ext=None, bulk=False, **extra):
        extra['HTTP_ACCEPT'] = self._get_japi_http_accept(bulk=bulk)

        return self.json_post(path=path, data=data, bulk=bulk, **extra)

    def json_delete(self, path, data=None, bulk=False, **extra):
        return super(TestClient, self).delete(
            path=path,
            data=data,
            follow=True,
            format='json',
            **extra
        )

    def japi_delete(self, path, data=None, bulk=False, **extra):
        extra['HTTP_ACCEPT'] = self._get_japi_http_accept(bulk=bulk)

        return self.json_delete(path=path, data=data, bulk=bulk, **extra)

    def json_patch(self, path, data=None, bulk=False, **extra):
        return super(TestClient, self).patch(
            path=path,
            data=data,
            follow=True,
            format='json',
            **extra
        )

    def japi_patch(self, path, data=None, bulk=False, **extra):
        extra['HTTP_ACCEPT'] = self._get_japi_http_accept(bulk=bulk)

        return self.json_patch(path=path, data=data, bulk=bulk, **extra)


class TestBase(APITestCase):

    def setUp(self):
        super(TestBase, self).setUp()

        self.client = TestClient()

    def result(self, response):
        return json.loads(response.content.decode('utf8'))
