from django.urls import path
from .views import sort, insertion_sort, selection_sort, merge_sort, quick_sort, contact_us, team, custom_sort

urlpatterns = [
    path("custom_comparision/", custom_sort, name='custom'),
    path('team/', team, name='team'),
    path('contact_us/', contact_us, name='contact'),
    path('quick_sort/', quick_sort, name='quick'),
    path('merge_sort/', merge_sort, name='merge'),
    path('selection_sort/', selection_sort, name='selection'),
    path('insertion_sort/', insertion_sort, name='insertion'),
    path('', sort, name='sort'),
]