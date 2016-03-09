from django.test import TestCase
from mock        import Mock
from user        import factories, models, middleware

class AnonboardUserMiddlewareTest(TestCase):

    def setUp(self):
        super(AnonboardUserMiddlewareTest, self).setUp()

        self.middleware = middleware.AnonboardUserMiddleware()
        self.user       = factories.UserFactory.create()
        self.request    = Mock()

    def tearDown(self):
        super(AnonboardUserMiddlewareTest, self).tearDown()

        self.user.delete()

    def test_get_user(self):
        self.request.META = {
            'REMOTE_ADDR':     self.user.ip,
            'HTTP_USER_AGENT': self.user.user_agent
        }

        self.assertIsNone(self.middleware.process_request(self.request))
        self.assertEqual(self.request.anonboard_user, self.user)

    def test_create_user(self):
        self.request.META = {
            'REMOTE_ADDR':     '127.0.0.1',
            'HTTP_USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0'
        }

        self.assertIsNone(self.middleware.process_request(self.request))
        self.assertIsInstance(self.request.anonboard_user, models.User)
        self.assertNotEqual(self.request.anonboard_user, self.user)
