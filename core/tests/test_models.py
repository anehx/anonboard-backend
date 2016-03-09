from django.test import TestCase
from core        import factories

class TopicModelTests(TestCase):

    def setUp(self):
        super(TopicModelTests, self).setUp()

        self.topic = factories.TopicFactory.create()

    def tearDown(self):
        super(TopicModelTests, self).tearDown()

        self.topic.delete()

    def test_to_str(self):
        self.assertEqual(str(self.topic), self.topic.name)


class ThreadModelTests(TestCase):

    def setUp(self):
        super(ThreadModelTests, self).setUp()

        self.thread = factories.ThreadFactory.create()

    def tearDown(self):
        super(ThreadModelTests, self).tearDown()

        self.thread.user.delete()
        self.thread.topic.delete()
        self.thread.delete()

    def test_to_str(self):
        self.assertEqual(str(self.thread), self.thread.title)


class CommentModelTests(TestCase):

    def setUp(self):
        super(CommentModelTests, self).setUp()

        self.comment = factories.CommentFactory.create()

    def tearDown(self):
        super(CommentModelTests, self).tearDown()

        self.comment.user.delete()
        self.comment.thread.topic.delete()
        self.comment.thread.delete()
        self.comment.delete()

    def test_to_str(self):
        self.assertEqual(
            str(self.comment),
            'Comment from %s to thread %s' % (
                str(self.comment.user),
                str(self.comment.thread)
            )
        )
