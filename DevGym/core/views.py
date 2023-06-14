from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth import logout


def home_view(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('logout.html')




# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

from django.shortcuts import render, redirect
from .models import Reservation
from datetime import datetime

from django.shortcuts import render, redirect
from .models import Reservation
from datetime import datetime
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Reservation
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Reservation

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Reservation

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Reservation

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Reservation
from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect
from .decorators import login_required_message


@login_required_message
def available_hours_view(request):
    reserved_hours = Reservation.objects.values_list('hour', flat=True)
    all_hours = []  # Aquí debes obtener todas las horas disponibles en algún formato

    available_hours = [hour for hour in all_hours if hour not in reserved_hours]

    if request.method == 'POST':
        selected_hour = request.POST.get('hour')
        if selected_hour:
            if request.user.is_authenticated:  # Verifica si el usuario está autenticado
                existing_reservations = Reservation.objects.filter(hour=selected_hour).count()
                if existing_reservations < 2:  # Verifica si hay menos de 2 reservas para la hora seleccionada
                    reservation = Reservation(user=request.user, hour=selected_hour)
                    reservation.save()
                    messages.success(request, 'Hora registrada exitosamente.')
                    return redirect('available_hours')
                else:
                    messages.error(request, 'No hay cupos disponibles para esta hora.')
                    return redirect('available_hours')

    return render(request, 'available_hours.html', {'hours': available_hours})

