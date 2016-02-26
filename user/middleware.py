from user.models import User

class AnonboardUserMiddleware(object):
    def process_request(self, request):
        ip         = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT')

        (user, created) = User.objects.get_or_create(ip=ip, user_agent=user_agent)

        setattr(request, 'anonboard_user', user)

        return None
