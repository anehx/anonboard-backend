from django.test import TestCase
from user        import factories

class UserModelTest(TestCase):

    def setUp(self):
        super(UserModelTest, self).setUp()

        self.user = factories.UserFactory.create()

    def tearDown(self):
        super(UserModelTest, self).tearDown()

        self.user.delete()

    def test_to_str(self):
        self.assertEqual(str(self.user), self.user.identifier)
