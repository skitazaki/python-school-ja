from django.http import HttpResponse
from django.template import Context, loader
from logviewer.models import Changeset
def home(request):
    changesets = Changeset.objects.all()
    t = loader.get_template('index.html')
    c = Context({'changesets': changesets})
    return HttpResponse(t.render(c))
