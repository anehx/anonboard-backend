from core.models           import Topic
from anonboard.test_helper import TestBase

class TopicTests(TestBase):
    def setUp(self):
        super(TopicTests, self).setUp()

        self.Foo = Topic.objects.create(name='Foo')
        self.Bar = Topic.objects.create(name='Bar')
        self.Baz = Topic.objects.create(name='Baz')


    def test_get_topic_list(self):
        response = self.client.japi_get('/api/v1/topics/')

        result = self.result(response)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(result['data']),    3)


    def test_get_topic(self):
        response = self.client.japi_get('/api/v1/topics/%i' % self.Foo.id)

        result = self.result(response)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['data']['attributes']['name'], 'Foo')
