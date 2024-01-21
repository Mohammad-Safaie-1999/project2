from django.shortcuts import render

def index_home(request):
    return render(request,'homepage.html')

def index_abilities(request):
    return render(request,'abilitiespage.html')

def index_contact(request):
    return render(request,'contactpage.html')

def index_education(request):
    return render(request,'educationpage.html')

def index_languages(request):
    return render(request,'languagespage.html')
