from django.shortcuts import render

from project_litter_bug_web.forms import ContactForm
from project_litter_bug_web.service import get_results_data, get_home_data, email_handler


def home(request):
    if request.method == 'GET':
        home_data = get_home_data()
        return render(request, 'templates/index.html', home_data)


def results(request):
    if request.method == 'GET':
        results_data = get_results_data(request)
        return render(request, 'templates/results.html', results_data)


def about(request):
    if request.method == 'GET':
        return render(request, 'templates/about.html', {})


def how_it_works(request):
    if request.method == 'GET':
        return render(request, 'templates/how-it-works.html', {})


def calculation(request):
    if request.method == 'GET':
        return render(request, 'templates/calculation.html', {})


def contact(request):
    form = ContactForm()
    result = False

    if request.method == 'POST':
        request, result, form = email_handler(request)
        if result:
            form = ContactForm()

    return render(request, 'templates/contact.html', {'form': form, 'result': result})


def donate(request):
    if request.method == 'GET':
        return render(request, 'templates/donate.html', {})



