from django.http import HttpResponse
from django.shortcuts import redirect

# The view-func is login_view or some other that we need
# The wrapper_func is used to write some checks, conditionals or operations and then call view_func
# It doesn't get executed until wrapper_func is executed
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('accounts_app:item_list')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to be here!')
            #print('Working:', allowed_roles)
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator
