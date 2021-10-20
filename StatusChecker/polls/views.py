from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Url


@login_required
def home(request):
    res = Url.objects.filter(user=request.user)
    context = {'res': res}
    return render(request, 'home.html', context)