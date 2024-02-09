from django.shortcuts import render
from .models import Notite
from django import forms
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


# Create your views here.


class NotiteProgram(forms.ModelForm):
    class Meta:
        model = Notite
        fields = ['id_notita', 'text_notita']


@csrf_exempt
def test(request):
    if request.method == 'GET':
        return HttpResponse("Merge")


@csrf_exempt
def aplicatie(request):
    return render(request, "index.html")


@csrf_exempt
def adugare_notite(request):
    if request.method == 'POST':
        new_id = Notite.objects.count()+1
        form = NotiteProgram(request.POST)
        copie = form.data.copy()
        copie['id_notita'] = new_id
        form.data = copie
        if form.is_valid():
            print(form.data)
            form.save()
        else:
            print("Invalid")
        return HttpResponse('yes')


@csrf_exempt
def afisare_numar(request):
    if request.method == 'POST':
        return JsonResponse({"Numar" : Notite.objects.count()})


@csrf_exempt
def afisare_notita(request):
    if request.method == 'POST':
        form = NotiteProgram(request.POST)
        copie = form.data.copy()
        numar = copie['id_notita']
        text = Notite.objects.filter(id_notita=numar).first()
        return JsonResponse({"Numar": numar,"Text": text.text_notita})






