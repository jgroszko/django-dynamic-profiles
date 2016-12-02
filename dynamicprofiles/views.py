from django.views.generic.list import ListView
from django.utils import timezone

from dynamicprofiles.models import Profile

class ProfileListView(ListView):
    model = Profile
    context_object_name = 'profiles'
