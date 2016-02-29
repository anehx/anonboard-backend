from django.test     import TestCase
from mock            import Mock
from user.middleware import AnonboardUserMiddleware
from user.models     import User

class AnonboardUserMiddlewareTest(TestCase):

    def setUp(self):
        self.middleware   = AnonboardUserMiddleware()
        self.request      = Mock()
        self.request.META = {
            'REMOTE_ADDR':     '127.0.0.1',
            'HTTP_USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0'
        }

    def test_process_request(self):
        self.assertIsNone(self.middleware.process_request(self.request))
        self.assertIsInstance(self.request.anonboard_user, User)
