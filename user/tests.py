from django.test     import TestCase
from mock            import Mock
from user.models     import User
from user.middleware import AnonboardUserMiddleware

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

class UserTest(TestCase):

    def setUp(self):
        self.ip         = '127.0.0.1'
        self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0'
        self.user_hash  = 'b0bd215ce6eae87e7368b9cb429349b41ee27ad3cdce35c3f74bea8dde2b52bb'
        self.user       = User.objects.create(ip=self.ip, user_agent=self.user_agent)

    def test_to_str(self):
        self.assertEqual(str(self.user), self.user.identification)

    def test_identification(self):
        self.assertEqual(self.user.identification, self.user_hash)
