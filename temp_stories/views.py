import random
from faker import Faker
from django.shortcuts import render

# Create your views here
# use f-strings for easy string formatting https://realpython.com/python-f-strings/ 

def story():
    fake = Faker()
    mystory = (
        f"In a(n) {fake.company()} a young {fake.language_name()} " 
        f"stumbles across a(n) {fake.domain_word()} which spurs him into conflict with {fake.name() }"
        f"an {fake.catch_phrase()} with the help of a(n) {fake.job()} and her {fake.file_name()}"
        f" culminating in a struggle at {fake.company()} where someone shouts: '{fake.bs()}'"
    )
    return mystory

def convert(temp):
    converted_temp = (temp-32)*0.5556
    return converted_temp

def compare(guess, number):
    answer = ""
    if guess < number:
        answer = "guess is low"
    elif guess > number:
        answer = "guess is high"
    else:
        answer = "you guesses correctly!"
    return answer


def index(request):
    mystory = story()
    converted_t = None
    temp = None
    if request.method== "POST":
        temp = int(request.POST.get('temp',''))
        converted_t = convert(temp)
    return render(request, 'temp_stories/index.html', {'story': mystory, 'converted_t': converted_t, 'temp': temp})

def guess(request):
    number = random.randint(1,10)
    guess = None
    answer = None
    if request.method == "POST":
        guess = int(request.POST.get('guess',''))
        answer = compare(guess, original)
    return render(request, 'temp_stories/guess.html', {'guess': guess, 'number': number, 'answer': answer})


