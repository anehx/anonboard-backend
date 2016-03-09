from django.test        import TestCase
from jsonapi.middleware import FilterMiddleware
from mock               import Mock


class FilterMiddlewareTest(TestCase):

    def setUp(self):
        self.middleware   = FilterMiddleware()
        self.request      = Mock()
        self.request.GET  = {
            'filter[foo]': 'bar',
            'bar':         'baz'
        }

    def test_process_request(self):
        self.assertIsNone(self.middleware.process_request(self.request))
        self.assertIsNone(self.request.GET.get('filter[foo]'))
        self.assertEqual(self.request.GET.get('foo'), 'bar')
        self.assertEqual(self.request.GET.get('bar'), 'baz')
