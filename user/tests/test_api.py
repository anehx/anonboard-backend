from anonboard.jsonapi_test_case import JSONAPITestCase
from user                        import factories


class UserAPITests(JSONAPITestCase):

    def setUp(self):
        super(UserAPITests, self).setUp()

        self.users = factories.UserFactory.create_batch(10)

    def tearDown(self):
        super(UserAPITests, self).tearDown()

        for user in self.users:
            user.delete()

    def test_get_user_list(self):
        response = self.client.get('/api/v1/users/')

        result = self.result(response)

        self.assertEqual(response.status_code, 200)

        # It has to return one more user than we created, because
        # the middleware creates a user for the test runner on the
        # first request
        self.assertEqual(len(result['data']), len(self.users) + 1)

    def test_get_user(self):
        response = self.client.get('/api/v1/users/%i' % self.users[0].id)

        result = self.result(response)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(result['data']['attributes']), 1)

        self.assertEqual(
            result['data']['attributes']['identifier'],
            self.users[0].identifier
        )
