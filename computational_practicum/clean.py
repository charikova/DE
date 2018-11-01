from computational_practicum.models import Post


def clean_db(request):
    Post.objects.all().delete()
