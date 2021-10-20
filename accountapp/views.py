from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld

def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request,
                      'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm #어떤 로그인 폼을 사용할 것인지 지정
    success_url = reverse_lazy('accountapp:hello_world')
    #성공하고 어디로 이동할 지 지정 # reverse는 함수형 base , reverse_lazy 객체형 base
    template_name = 'accountapp/create.html'
    #성공했을 때 보여줄 페이지

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm #어떤 로그인 폼을 사용할 것인지 지정
    success_url = reverse_lazy('accountapp:hello_world')
    #성공하고 어디로 이동할 지 지정 # reverse는 함수형 base , reverse_lazy 객체형 base
    template_name = 'accountapp/update.html'
    #성공했을 때 보여줄 페이지