from django.shortcuts import render
from .models import Enquete
# Create your views here.

def index(request):
    return render(request,'bemvindo.html')

def bemvindo(request):
    return render(request,'bemvindo.html')

def exibirEnquete(request,enquete_id):
    enquete = Enquete()

    if enquete_id == 1:
        enquete = Enquete(enquete_id,'Você prefere suco de maracujá ou suco de uva ?','27/08/2020')
    if enquete_id == 2:
        enquete = Enquete(enquete_id,'Você tem preferencia por notebook ou computador de mesa?','20/08/2020')
    if enquete_id == 3:
        enquete = Enquete(enquete_id,'você prefere água com açucar ou chá para se acalmar?','23/08/2020') 

    return render(request,'enquete.html',{'enquete':enquete})
