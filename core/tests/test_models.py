from core.models import Topic
from django.test import TestCase

class TopicModelTests(TestCase):

    def test_to_str(self):
        topic = Topic.objects.create(name='Test')
        self.assertEqual(str(topic), 'Test')
