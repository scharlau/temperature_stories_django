from faker import Faker
from django.shortcuts import render

# Create your views here
# use f-strings for easy string formatting https://realpython.com/python-f-strings/ 

def story():
    fake = Faker()
    mystory = (
        f"In a(n) {fake.company()} a young {fake.language_name()}" 
        f"stumbles across a(n) {fake.domain_word()} which spurs him into conflict with {fake.name() }"
        f"an {fake.catch_phrase()} with the help of a(n) {fake.job()} and her {fake.file_name()}"
        f" culminating in a struggle at {fake.company()} where someone shouts {fake.bs()}"
    )
    return mystory

def index(request):
    mystory = story()
    converted_t = None
    temp = None
    if request.method== "POST":
        temp = int(request.POST.get('temp',''))
        converted_t = (temp-32)*0.5556
    return render(request, 'temp_stories/index.html', {'story': mystory, 'converted_t': converted_t, 'temp': temp})

