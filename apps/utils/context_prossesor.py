from apps.models import User


def context_user(request):
    return {
        "categories": User.objects.all(),
    }
