from faker import Faker
from django.shortcuts import render

# Create your views here.

def story():
    fake = Faker()
    mystory =   "In a(n) " + fake.company()
    mystory = mystory + " a young "
    mystory = mystory + fake.language_name()
    mystory = mystory + " stumbles across a(n) "
    mystory = mystory + fake.domain_word()
    mystory = mystory +  " which spurs him into conflict with " 
    mystory = mystory + fake.name() 
    mystory = mystory + " an " + fake.catch_phrase()
    mystory = mystory + " with the help of a(n) "
    mystory = mystory + fake.job()
    mystory = mystory + " and her "
    mystory = mystory + fake.file_name() 
    mystory = mystory + " culminating in a struggle at "
    mystory = mystory + fake.company()
    mystory = mystory + " where someone shouts "
    mystory = mystory + fake.bs()
    return mystory

def index(request):
    mystory = story()
    converted_t = None
    temp = None
    if request.method== "POST":
        temp = int(request.POST.get('temp',''))
        converted_t = (temp-32)*0.5556
    return render(request, 'temp_stories/index.html', {'story': mystory, 'converted_t': converted_t, 'temp': temp})

