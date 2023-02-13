from django.urls import path

from .views import ProfilesListView, load_states

urlpatterns = [
    # path('', ProfilesListView.as_view()),
    path('', ProfilesListView.as_view(), name='index'),
    path('states', load_states, name='states'),
]
