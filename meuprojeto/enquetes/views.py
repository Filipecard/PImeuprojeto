from django.shortcuts import render,get_object_or_404
from .models import Enquete
# Create your views here.

def index(request):
    return render(request,'bemvindo.html')

def bemvindo(request):
    return render(request,'bemvindo.html')

def exibirEnquete(request,enquete_id):
    try:
        enquete = get_object_or_404(Enquete,pk = enquete_id)
        return render(request,'enquete.html',{'enquete':enquete})
    except:
        enquete = Enquete('nula','não encontrado','0000-00-00')
        return render(request,'enquete.html',{'enquete':enquete})
