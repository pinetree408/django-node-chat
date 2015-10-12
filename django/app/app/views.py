from django.views.generic import ListView
from chat import models


class IndexView(ListView):
    queryset = models.Room.objects.all()[:10]
    template_name = "index.html"
