from django.shortcuts import render
from lettings.models import Letting

    
def index(request):
    template_name = 'lettings/index.html'
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, template_name, context)

def letting(request, letting_id):
    template_name = 'lettings/letting.html'
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
        'url_image': letting.URL,
        'type': letting.type,
    }
    return render(request, template_name, context)
