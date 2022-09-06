from django.views import generic

from .models import Character


class IndexView(generic.ListView):
    template_name = 'wh_info/index.html'
    context_object_name = "character_list"

    def get_queryset(self):
        return Character.objects.all()

# class DetailView()
