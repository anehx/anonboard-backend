import unittest

from anonboard.jsonapi_test_case import JSONAPITestCase
from core                        import factories


class TopicAPITests(JSONAPITestCase):

    def setUp(self):
        super(TopicAPITests, self).setUp()

        self.topics = factories.TopicFactory.create_batch(10)

    def tearDown(self):
        super(TopicAPITests, self).tearDown()

        for topic in self.topics:
            topic.delete()

    def test_get_topic_list(self):
        response = self.client.get('/api/v1/topics/')

        result = self.result(response)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(result['data']), len(self.topics))

    def test_get_topic(self):
        response = self.client.get('/api/v1/topics/%i' % self.topics[0].id)

        result = self.result(response)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            result['data']['attributes']['name'],
            self.topics[0].name
        )

        self.assertEqual(
            result['data']['attributes']['identifier'],
            self.topics[0].identifier
        )

        self.assertEqual(
            result['data']['attributes']['description'],
            self.topics[0].description
        )


class ThreadAPITests(JSONAPITestCase):

    def setUp(self):
        super(ThreadAPITests, self).setUp()

        self.threads = factories.ThreadFactory.create_batch(10)

    def tearDown(self):
        super(ThreadAPITests, self).tearDown()

        for thread in self.threads:
            thread.delete()

    def test_get_thread_list(self):
        response = self.client.get('/api/v1/threads/')

        result = self.result(response)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(result['data']), len(self.threads))

    def test_get_thread(self):
        response = self.client.get('/api/v1/threads/%i' % self.threads[0].id)

        result = self.result(response)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            result['data']['attributes']['title'],
            self.threads[0].title
        )

        self.assertEqual(
            result['data']['attributes']['content'],
            self.threads[0].content
        )

    @unittest.skip('Not implemented yet')
    def test_post_thread(self):
        data = {
            'data': {
                'type': 'threads',
                'attributes': {
                    'title': 'Foo',
                    'content': 'Foo'
                },
                'relationships': {
                    'topic': {
                        'data': {
                            'type': 'topic',
                            'id': 1
                        }
                    }
                }
            }
        }

        response = self.client.post('/api/v1/threads/', data, format='json')

        # result = self.result(response)

        self.assertEqual(response.status_code, 201)


class CommentAPITests(JSONAPITestCase):

    def setUp(self):
        super(CommentAPITests, self).setUp()

        self.comments = factories.CommentFactory.create_batch(10)

    def tearDown(self):
        super(CommentAPITests, self).tearDown()

        for comment in self.comments:
            comment.delete()

    def test_get_comment_list(self):
        response = self.client.get('/api/v1/comments/')

        result = self.result(response)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(result['data']), len(self.comments))

    def test_get_comment(self):
        response = self.client.get('/api/v1/comments/%i' % self.comments[0].id)

        result = self.result(response)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            result['data']['attributes']['content'],
            self.comments[0].content
        )
