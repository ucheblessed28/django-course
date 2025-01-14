from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request):
    '''View function for the home page. It renders the home.html template
    and passes dynamic data to the template.'''

    # Dynamic data to pass to the template

    context = {
        'title': 'Welcome to My Website',
        'description': 'This is a simple example of passing data to a template.',
        'heading': 'This is the home page',
        'paragraph': 'This is a simple website created using Django framework.',
        'author': 'John Doe',
        'date': 'July 12, 2023',
        'footer': '�� 2023 My Website. All rights reserved.',
        'social_media': [
            {'name': 'Facebook', 'url': 'https://www.facebook.com/mywebsite'},
            {'name': 'Twitter', 'url': 'https://www.twitter.com/mywebsite'},
            {'name': 'Instagram', 'url': 'https://www.instagram.com/mywebsite'},
        ],
    }
    return render(request, 'home.html', context)