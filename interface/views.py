from django.shortcuts import render, redirect
from .models import Assistance, CanAssist

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import AssistanceSerializer, CanAssistSerializer


# Create your views here.
def home(request):
    return render(request, 'interface/index.html')

def success(request):
    return render(request, 'interface/success.html')

def assistance(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        addr1 = request.POST['address1']
        addr2 = request.POST['address2']
        city = request.POST['city']
        state = request.POST['state']
        pin = request.POST['pin']
        phone_number = request.POST['phone_number']
        assistance_needed = request.POST['assistance_needed']
        message = request.POST['message']

    # Saving entries
        entry = Assistance.objects.create(email=email,name=name,addr1=address,addr2=address2,city=city,
        state=state,pin=pin,phone_number=phone_number,assistance_needed=assistance_needed,message=message)
        entry.save()

        return redirect('success')
    return render(request, 'interface/assistance.html')

def can_assist(request):
    return render(request, 'interface/can_assist.html')

class AssistanceViewSet(viewsets.ModelViewSet):
    
    queryset = Assistance.objects.all()
    serializer_class = AssistanceSerializer

class CanAssistViewSet(viewsets.ModelViewSet):
    
    queryset = CanAssist.objects.all()
    serializer_class = CanAssistSerializer
     