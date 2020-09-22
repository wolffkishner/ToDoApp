from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticatedUser(view_func):
    def wrapperFunc(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapperFunc
