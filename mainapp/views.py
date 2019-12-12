from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import json
from django.views.decorators.csrf import csrf_exempt
from mainapp.models import Contestant


# Create your views here.


def index(request):
    return render(request, 'index.html')


def contestant(request):
    contestants = Contestant.objects.filter(approved=True).order_by('-id')

    if request.GET.get('full_name') :
        contestants = contestants.filter(full_name__icontains=request.GET.get('full_name'))
    if request.GET.get('county') not in ['All', None]:
        contestants = contestants.filter(county=request.GET.get('county').lower())
    return render(request, 'contestant.html', {'contestants': contestants})


def schedule(request):
    return render(request, 'schedule.html')


def partners(request):
    return render(request, 'partners.html')


def crew(request):
    return render(request, 'crew.html')


def success(request):
    return render(request, 'success.html')


def validate(data):
    if Contestant.objects.filter(phone=data.get('phone')).exists():
        return False, 'phone exists'
    if Contestant.objects.filter(ig_username=data.get('ig_username')).exists():
        return False, 'instagram account exists'
    return True, ''


def reg_form(request):
    if request.method == 'POST':
        validation, error = validate(request.POST)
        if not validation:
            return render(request, 'register.html', {'error': error})
        full_name = request.POST.get('full_name')
        ig_username = request.POST.get('ig_username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender').lower()
        county = request.POST.get('county').lower()
        image = request.FILES.get('image')
        Contestant.objects.create(full_name = full_name, ig_username =ig_username, email = email, phone = phone, county=county, gender=gender, image=image)
        return redirect('success')
    return render(request, 'register.html')

@login_required(login_url='/admin/')
def dashboard(request):
    contestants = Contestant.objects.all()
    if request.method == 'POST':
        ids = request.POST.getlist('approved')
        for contestant in contestants:
            contestant.approved = False
            if str(contestant.id) in ids:
                contestant.approved = True
            contestant.save()
    if request.GET.get('gender') not in ['All',None]:
        contestants = contestants.filter(gender = request.GET.get('gender').lower())
    if request.GET.get('county') not in ['All',None]:
        contestants = contestants.filter(county = request.GET.get('county').lower())
    return render(request, 'dashboard.html', {'contestants': contestants})
