import slug as slug
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .forms import SuperModelForm
from django.core.paginator import Paginator

@login_required
def my_view(request):
    my_queryset = MyModel.objects.all()
    paginator = Paginator(my_queryset, 2)  # показывать 25 объектов на странице
    page = request.GET.get('page')  # получить текущую страницу из параметров URL
    my_objects = paginator.get_page(page)
    response = render(request, 'stranica.html', context={'users': my_objects})
    response = set_cookie(request, response)
    return response


from .models import News, MyModel, VisitedPage




def logout(request):
    if request.user.is_authenticated:
        visited_pages = []
        visited_cookies = request.COOKIES.get('visit_count')
        if visited_cookies:
            visited_pages = visited_cookies.split(',')
        for page in visited_pages:
            VisitedPage.objects.create(user=request.user, page_name=page)
        response = redirect('accounts/login')
        response.delete_cookie('visited_pages')
        return response
    else:
        return redirect('login')

def news(request):
    user = News.objects.all()
    response = render(request, 'stranica.html', context={'new': user})
    response = set_cookie(request, response)
    return response

# Create your views here.
def index(request):
    return render(request, "ashtimeel.html")


def addnews(request):
    if request.method == 'POST':
        form = SuperModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = SuperModelForm()
    return render(request, 'ashtimeel.html', {'form': form})


class MyDetailView(DetailView):
    model = News
    template_name = 'nvrw.html'
    context_object_name = 'name'
    slug_field = 'slug'


def setcookie(request):
    html = HttpResponse("<h1>Hello</h1>")
    html.set_cookie('CookieName', 'Hello this is your Cookies', max_age=None)
    return html

def set_cookie(request, response):
    if request.COOKIES.get('visit_count'):
        visit_count = int(request.COOKIES.get('visit_count')) + 1
    else:
        visit_count = 1
    response.set_cookie('visit_count', str(visit_count))
    return response

def deletecookie(request) :
    html = HttpResponse("<h1>Cookies Deleted</h1>")
    html.delete_cookie('visit_count')
    return html

from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UserForm


class UserRegister(CreateView):
    model = User
    template_name = 'registration/reg.html'
    form_class = UserForm
    success_url = reverse_lazy('login')