from rest_framework.test import APITestCase, APIClient

import json


class JSONAPIClient(APIClient):

    def _parse_data(self, data):
        return json.dumps(data) if data else data

    def japi_get(self, path, data=None, **extra):
        return super(JSONAPIClient, self).get(
            path=path,
            data=self._parse_data(data),
            content_type='application/vnd.api+json',
            **extra
        )

    def japi_post(self, path, data=None, **extra):
        return super(JSONAPIClient, self).post(
            path=path,
            data=self._parse_data(data),
            content_type='application/vnd.api+json',
            **extra
        )

    def japi_delete(self, path, data=None, **extra):
        return super(JSONAPIClient, self).delete(
            path=path,
            data=self._parse_data(data),
            content_type='application/vnd.api+json',
            **extra
        )

    def japi_patch(self, path, data=None, **extra):
        return super(JSONAPIClient, self).patch(
            path=path,
            data=self._parse_data(data),
            content_type='application/vnd.api+json',
            **extra
        )


class JSONAPITestCase(APITestCase):

    def setUp(self):
        super(JSONAPITestCase, self).setUp()

        self.client = JSONAPIClient()

    def result(self, response):
        return json.loads(response.content.decode('utf8'))
