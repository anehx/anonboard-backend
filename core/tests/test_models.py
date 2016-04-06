from django.test  import TestCase
from django.utils import timezone
from core         import factories


class TopicModelTests(TestCase):

    def setUp(self):
        super(TopicModelTests, self).setUp()

        self.topic = factories.TopicFactory.create()

    def tearDown(self):
        super(TopicModelTests, self).tearDown()

        self.topic.delete()

    def test_threads_last_day(self):
        invalid_threads = factories.ThreadFactory.create_batch(
            size=5,
            topic=self.topic
        )

        valid_threads = factories.ThreadFactory.create_batch(
            size=5,
            topic=self.topic
        )

        two_days_ago = timezone.now() - timezone.timedelta(days=2)

        for thread in invalid_threads:
            thread.created = two_days_ago
            thread.save()

        self.assertEqual(self.topic.threads_last_day, len(valid_threads))

    def test_to_string(self):
        self.assertEqual(str(self.topic), self.topic.name)


class ThreadModelTests(TestCase):

    def setUp(self):
        super(ThreadModelTests, self).setUp()

        self.thread = factories.ThreadFactory.create()

    def tearDown(self):
        super(ThreadModelTests, self).tearDown()

        self.thread.delete()

    def test_to_string(self):
        self.assertEqual(str(self.thread), self.thread.title)


class CommentModelTests(TestCase):

    def setUp(self):
        super(CommentModelTests, self).setUp()

        self.comment = factories.CommentFactory.create()

    def tearDown(self):
        super(CommentModelTests, self).tearDown()

        self.comment.delete()

    def test_to_string(self):
        self.assertEqual(
            str(self.comment),
            'Comment from %s to thread %s' % (
                str(self.comment.user),
                str(self.comment.thread)
            )
        )
