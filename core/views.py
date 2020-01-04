from django.shortcuts import render
from django.views import View


class HomeView(View):
    @staticmethod
    def get(request):
        context = {}
        return render(request, 'core/home.html', context)
