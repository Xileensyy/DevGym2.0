from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect

def login_required_message(function):
    @wraps(function)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Necesitas iniciar sesión para acceder a esta página.')
            return redirect('login')
        return function(request, *args, **kwargs)
    return wrapper
