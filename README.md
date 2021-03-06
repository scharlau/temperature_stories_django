# Temperature Stories with Python Django
A 'deliberate practice' exercise with python web framework Django that converts temperatures and generates stories. This example walks you through building a basic Django application without a database.

The goal of 'deliberate practice' is to think about how you'd solve this challenge, and to work at developing code to make this work. There is no single 'correct' version of this code. The purpose of the exercise it become familiar with different ways of making the application work. You should explore how this simple application is done in Rails so that you understand how variables in controllers are show up in the views you see in the browser.

Under 'deliberate practice' we offer up the challenge, then think about options for developing a solution, and code for 12 minutes. After that we pause to discuss how people are approaching the problem, and what they're trying to do. This should be repeated three times and then wrapped up with time for people to express what they found most useful during the session. This should take an hour.

# First, create the basics
Create a new project folder called 'temperature_stories' and then cd into the folder via the terminal and execute these commands:

    pyenv local 3.7.0 # this sets the local version of python to 3.7.0
    python3 -m venv .venv # this creates the virtual environment for you
    source .venv/bin/activate # this activates the virtual environment
    pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.

We will use Django (https://www.djangoproject.com) as our web framework for the application. We install that with 
        
        pip install Django==3.1.3
    
And that will install django version 3.1.3 (or pick a different version if there's something newer) with its associated dependencies. We can now start to build the application.

Now we can start to create the site using the django admin tools. Issue this command, and don't forget the '.' at the end of the line, which says 'create it in this directory'. This will create the admin part of our application, which will sit alongside the actual site. 

        django-admin startproject mysite .

We're using the name 'mysite' but you could use whatever seems appropriate. We'll save the temperature-stories' label for later in the app. For now we're setting up the support structure for the site, which will live in a separate folder.

We need to specify some settings for the site, which we do in the mysite/settings.py file. Open this and add this line above the line for pathlib import Path:

        import os

Now go to the end of the file to add a line specifying the root directory for the static files.

        STATIC_ROOT = os.path.join(BASE_DIR, 'static')

Now go further up the file to 'ALLOWED_HOSTS' so that we can run this beyond 'localhost' and 127.0.0.1, which are the only allowed ones if this is empty. Modify this accordingly to suit your needs:

        ALLOWED_HOSTS = ['word-otherword.herokuapp.com', 'localhost']

We now need to configure the database, which you saw was already detailed in the settings.py file. As django has a built-in admin tool, it already knows some of the tables that it needs to use. We can set this up with the command:

        python3 manage.py migrate

You should see a number of steps being run, each hopefully ending ... OK
If not, then look to the errors in the terminal. If you see one that says 'NameError: name 'os' is not defined', then go back and add the import for the 'os' library.

## Start the Server

We so this using the manage.py command tool by entering this command in the terminal:

        python3 manage.py runserver

If you're doing this on another platform, then you might need to use this instead (change the port number from 8000 as required):

        python3 manage.py runserver 0.0.0.0:8000 

If it went well, then you should see the python rocket launching your site. 

## Creating the Story content

Leave the server running. Open a new terminal and navigate as required to the same directory. We can now set about creating the space for our temperature stories by running this command:

        python3 manage.py startapp temp_stories

This will create a new folder fo us including space for database migrations, and other details specific to our content. By the way, we need to use an underscore to join the words in temp_stories as a hyphen is not allowed as part of an identifier.

Django needs to know the urls of the site so that it can serve up pages to visitors, and tell others that the page requested isn't part of the site. We do that by opening mysite/urls.py and adding a line for the pages that will be under temp_stories. 

First, add 'include' to the line with 'import path' so that it reads 

        from django.urls import path, include

Second, add this line (plus the , at the end of the line above it), to have django find your temp_stories pages:

        path('', include('temp_stories.urls')),

Third, we need to modify the settings.py file in the mysite app, so that it knows to include the 'temp_stories' contents. We do this by adding a line in the section on 'INSTALLED_APPS'. Add this line to the end of the block ( plus the , at the end of the line above it).

        'temp_stories.app.TempStoriesConfig',

We can now start the logic for our application. Before we do that we need to add the Faker library to our application with the command:

        pip install faker

In Django applications the logic goes into the 'views.py' file. Here we'll add each of the methods that returns a page in our application. Open the file temp_stories/views.py  add this code:

        from faker import Faker
        from django.shortcuts import render

        # Create your views here.
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
                return render(request, 'temp_stories/index.html', {'story': mystory})

As you can see this is similar to the code we used in the flask version of the site. The only differences are that we're now passing in the 'request' object to the index method, and use that in the template rendering, and we also create a dictionary object to pass to the template. The ideas are the same, but the syntax is slightly different.

For the templates we need to put the index.html file into a 'templates' directory. Create that, and then create a 'temp_stories' directory under 'templates'. This is a Django convention, and helps us separate out the content for our site if we added other components to the site. 

Now create a blank index.html file and put this code into it. This is almost the same as what we used in the flask version. We've only changed the text in the file.

        <!DOCTYPE html>
        <html><head>
        <title>Temperature Story Generator</title>
        </head><body>
 
        <h1>Temperature Story Generator</h1>
        <p>
        {{ story }}
        </p>
        </body></html>

We are now ready to run the changes to see the page load. Stories should now appear when you load the page on the site.

## Adding in the temperature conversion

We can add a form to the page so that we can add a temperature conversion that's added to the story. Weird, but it makes the exercise interesting.

Open up views.py and add modify the index method so that it looks like this:

        def index(request):
                mystory = story()
                converted_t = None
                temp = None
                if request.method== "POST":
                        temp = int(request.POST.get('temp',''))
                        converted_t = (temp-32)*0.5556
                return render(request, 'temp_stories/index.html', {'story': mystory, 'converted_t': converted_t, 'temp': temp})

This now accepts the variable 'temp' from the form and converts it to 'converted_t' to send back to the page for display.

Open up index.html and modify the page to look like this:

        <body>
        <h1>Temperature Story Generator</h1>
        <form action="/" method="post">
        {% csrf_token %}
        <p>Enter the temperature in fahrenheit to convert to celsius:</p>
        <input type="number" name="temp">
        <input type="submit" value="Convert">
        </form>
        <p>{{ story }}</p>
        <p>Your converted temperature of {{ temp }} in F is {{ converted_t }} in C</p>
        </body>

Save the changes, and reload the pages to see it in action.

## Do Some of your own changes

We're now ready for you to modify the site to learn a bit more about how you use Django and understand the relationship between the components. This is mostly a quick intro without models and tables to show how you might use Django this way.

You can take this further in three stages:
1. Clean up the code in views.py by moving the temperature convertion to a separate method so that you can add the two temperatures to the story, and still display the 'conversion sentence' too.
2. Separate out the temperature conversion as a new app in 'mysite' that is called 'convert' and has a form for converting temperatures from farhrenheit to celsius.
3. Push the boundaries further to see what else you might do with Django.