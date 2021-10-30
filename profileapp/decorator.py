from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request,*args,**kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])  #pk를 받아서 이 프로파일의 주인을 확인
        if not profile.user == request.user: #이 프로필 유저가, 요청의 유저와 같지 않다면,
            return HttpResponseForbidden() #포비든
        return func(request,*args,**kwargs) # 아니면 그대로~ 보내주셈
    return decorated

