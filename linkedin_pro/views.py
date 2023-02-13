from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView

from .models import States, Countries
from .serializers import LinkedinProfiles


class ProfilesListView(ListView):
    model = LinkedinProfiles
    template_name = 'index.html'
    paginate_by = 2

    def get(self, request, *args, **kwargs):

        countries = Countries.objects.all()
        country_id = request.GET.get('country')
        if country_id is not None:
            country_id = int(request.GET.get('country'))
        state_id = request.GET.get('state')
        states = States.objects.filter(country_id=country_id)
        if state_id is not None:
            state_id = int(request.GET.get('state'))
        phone = request.GET.get('phone')
        email = request.GET.get('email')
        name = request.GET.get('name')
        query_obj = {'country': country_id, 'state': state_id, 'name': name, 'phone': phone, 'email': email}
        if name == '':
            name = None
        print(query_obj)
        profiles = fetch_profiles(country_id, state_id, name, phone, email)
        paginator = Paginator(profiles, 50)  # Show 50 profiles per page
        page = request.GET.get('page')
        profiles = paginator.get_page(page)
        page_obj = paginator.get_page(page)
        return render(request, self.template_name,
                      {'countries': countries, 'profiles': profiles, 'states': states, 'query_obj': query_obj,
                       'page_obj': page_obj})


def fetch_profiles(country_id, state_id, name, phone, email):
    filters = {}
    if phone == 'true':
        filters['primary_number__isnull'] = False
    if email == 'true':
        filters['primary_email__isnull'] = False
    profiles = LinkedinProfiles.fetch(country_id=country_id, state_id=state_id, names_vector=name, **filters)
    return profiles


def load_states(request):
    country_id = request.GET.get('country')
    states = States.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'states.html', {'states': states})
