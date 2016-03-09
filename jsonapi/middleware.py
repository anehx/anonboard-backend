import re


class FilterMiddleware(object):
    def process_request(self, request):
        request.GET = request.GET.copy()

        filters_dict = {}
        removed_keys = []
        for key in request.GET:
            if key.startswith('filter['):
                match = re.match(
                    r'filter\[(.*?)\].*',
                    key)
                filters_dict[match.group(1)] = request.GET[key]
                removed_keys.append(key)

        for removed_key in removed_keys:
            request.GET.pop(removed_key)

        request.GET.update(filters_dict)

        return None
