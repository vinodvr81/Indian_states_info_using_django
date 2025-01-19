from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# from django.template import loader
from .models import StatesInfo

def home(request):
    # Logic for home view, maybe render a template or redirect
    return render(request, 'master.html')  # Or any other logic you want

def state_info(request):
    states_names = StatesInfo.objects.values_list('state_name', flat=True)  # Fetch state names
    city_cap = StatesInfo.objects.values_list('city_name', flat=True)  # Fetch city names
    pop_no = StatesInfo.objects.values_list('population_no', flat=True)  # Fetch population numbers
    combined_data = zip(states_names, city_cap, pop_no)
    context = {'combined_data': combined_data}
    return render(request, 'all_states.html', context)

def no_four(request):
    return render(request, '404.html', {})
