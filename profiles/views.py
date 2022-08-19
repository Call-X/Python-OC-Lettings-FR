from django.shortcuts import render
from profiles.models import Profile

   
def index(request):
    template_name = 'profiles/index.html'
   
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, template_name , context) 

def profile(request, username):
    template_name = 'profiles/profile.html'
    
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, template_name, context)

