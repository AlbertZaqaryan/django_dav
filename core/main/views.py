from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import HomeSlider
# Create your views here.


class HomeSliderListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        sliders = HomeSlider.objects.all()
        return render(request, self.template_name, {'sliders':sliders})