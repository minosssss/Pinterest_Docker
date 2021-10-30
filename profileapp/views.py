from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorator import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:detail')
    #detail로 가야 하지만, accoutapp의 url을 보면 pk를 받아야 하기에 get success_url 을 추가 해준다
    template_name = 'profileapp/create.html'

    def form_valid(self, form): #제출을 눌렀을 때, 받는 form (image,nickname,message)
        temp_profile = form.save(commit=False) #임시데이터 저장
        temp_profile.user = self.request.user #임시유저를 보낸 유저로 저장
        temp_profile.save() #최종저장
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})
        #self.object가 가르키는 것은 ProfileCreateView의 model(Profile)=User이다.
        #그 user의 pk를 찾아서 넘겨줘라.

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk})