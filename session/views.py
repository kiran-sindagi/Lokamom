from django.shortcuts import render

# Create your views here.
def Letter(request):
    return render(request, "letter.html")

def whatWeOffer(request):
    return render(request, 'sessions.html')

def oneOnOne(request):
    return render(request, "one.html")

def groupSession(request):
    return render(request, "group.html")

def StressSession(request):
    return render(request, "stress_management.html")