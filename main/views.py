from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Estate, Realtor, EstateImages
from .forms import EstateFilterForm, EstateForm, RealtorForm


def home(request):
    return render(request, 'main/home.html')


def objects(request):
    estates = Estate.objects.all()
    if request.method == 'POST':
        form = EstateFilterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            type_of_object = cd['type_of_object']
            type_of_deal = cd['type_of_deal']
            print(cd)
            if type_of_object == 'ALL' and type_of_deal != 'ALL':
                estates = Estate.objects.filter(type_of_deal=type_of_deal)
            elif type_of_object != 'ALL' and type_of_deal == 'ALL':
                estates = Estate.objects.filter(type_of_estate=type_of_object)
            elif type_of_object == 'ALL' and type_of_deal == 'ALL':
                estates = Estate.objects.all()
            else:
                estates = Estate.objects.filter(type_of_estate=type_of_object, type_of_deal=type_of_deal)
            form = EstateFilterForm(
                initial={'type_of_object': cd['type_of_object'], 'type_of_deal': cd['type_of_deal']})
            return render(request, 'main/objects.html', {'estates': estates, 'form': form})

    form = EstateFilterForm()
    return render(request, 'main/objects.html', {'estates': estates, 'form': form})


def detail(request, estate_id):
    estate = get_object_or_404(Estate, pk=estate_id)
    return render(request, 'main/detail.html', {'estate': estate})


def team(request):
    realtors = Realtor.objects.all()
    return render(request, 'main/team.html', {'realtors': realtors})


@staff_member_required
def add_object(request):
    if request.method == 'POST':
        form = EstateForm(request.POST, request.FILES)
        if form.is_valid():
            estate = form.save()
            images = request.FILES.getlist('image_field')
            for i in images:
                EstateImages.objects.create(estate=estate, image=i)
            return redirect('main:objects')
    form = EstateForm()
    return render(request, 'main/add_object.html', {'form': form})


@staff_member_required
def add_realtor(request):
    if request.method == 'POST':
        form = RealtorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:team')
    form = RealtorForm()
    return render(request, 'main/add_realtor.html', {'form': form})
