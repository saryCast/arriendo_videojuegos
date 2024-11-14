from django.shortcuts import render,redirect,get_object_or_404
from  django.views import View
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from web.models import *
from .forms import PlataformaForm

# Create your views here.


class RegisterView(View):
    def get(self, request):
        return render(request,'registration/register.html')
    
    def post(self, request):
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1 != password2:
            messages.error(request,'passwords do not match')
            return redirect(reverse('register'))
        user=User.objects.create_user(username=email, email=email, password=password1, first_name=first_name, last_name=last_name)
         #user.is_active = False
        
        user.save()
        user = authenticate(username=email, password=password1)
        if user is not None:
            login(request, user)
        messages.success(request, 'Usuario creado exitosamente')
        return redirect('index')
class CustomLoginView(SuccessMessageMixin, LoginView):
    success_message = "Sesion Iniciada Exitosamente"
    template_name = 'registration/login.html'  
    redirect_authenticated_user = True
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.WARNING, "Sesion Cerrada Exitosamente")
        return response
    

@login_required
def index(request):
    form=PlataformaForm(request.GET)
    if form.is_valid():
        plataforma=form.cleaned_data.get('plataforma')

        if plataforma:
            juegos=Juego.objects.filter(plataforma=plataforma)
        else:
            juegos=Juego.objects.all().filter(arrendador__isnull=True)
    else:
        juegos=Juego.objects.all()

    return render(request,'index.html',{'juegos':juegos,'form':form})

@login_required
def arrendar(request, id):
    juego = get_object_or_404(Juego, id=id)

    if request.method == 'POST':
    
        fecha = request.POST.get('fecha')
        fecha_seleccionada = timezone.datetime.strptime(fecha, "%Y-%m-%d").date()
        fecha_hoy = timezone.now().date()
        
        if fecha_seleccionada < fecha_hoy:
            messages.error(request, "La fecha seleccionada debe ser hoy o una fecha futura.")
            return render(request, 'arrendar.html', {'juego': juego})
       
        nuevo_arriendo = Arriendo.objects.create(fecha_arriendo=fecha, user=request.user, juego=juego)

        juego.arrendador = request.user
        juego.save()
        
        return redirect('index')  
    return render(request, 'arrendar.html', {'juego':juego})

@login_required
def misArriendos(request):
    arriendos = Arriendo.objects.filter(user=request.user, fecha_devolucion__isnull=True)
    return render(request,'mis_arriendos.html',{'arriendos':arriendos})

@login_required
def retornar(request,id):
    arriendo=get_object_or_404(Arriendo, id=id)
    return render(request,'retornar.html',{'arriendo':arriendo})  


@login_required
def devolver(request, id):
    arriendo = get_object_or_404(Arriendo, id=id)
    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        fecha_seleccionada = timezone.datetime.strptime(fecha, "%Y-%m-%d").date()

        fecha_arriendo= arriendo.fecha_arriendo.date()

        if fecha_seleccionada <= fecha_arriendo:
            messages.error(request, "La fecha seleccionada debe ser superior a la fecha de arriendo")
            return render(request, 'retornar.html', {'arriendo': arriendo})

        dias_retraso = (fecha_seleccionada - fecha_arriendo).days - arriendo.juego.plataforma.dias_arriendo
        if  dias_retraso>0:
            deuda=dias_retraso*arriendo.juego.plataforma.precio_dias_atraso
        else:
            deuda=0
            dias_retraso = 0

        arriendo.fecha_devolucion=fecha_seleccionada
        arriendo.multa = deuda
        arriendo.save()
        juego=arriendo.juego
        juego.arrendador=None
        juego.save()
        

        if deuda > 0:
            messages.success(request, f"El juego {arriendo.juego.titulo} se retornó con {dias_retraso} días de retraso, generando ${deuda} de multa.")
        else:
            messages.success(request, f"El juego {arriendo.juego.titulo} se retornó sin retraso.")

        return redirect('mis_arriendos')

    return render(request, 'retornar.html', {'arriendo': arriendo})


@login_required
def reporteArriendos(request):
    if not request.user.is_staff:
        messages.error(request, "No tienes permisos para ver los arriendos.")
        return redirect('index')
    
    arriendos = Arriendo.objects.select_related('juego', 'user').order_by('fecha_devolucion')
    return render(request, 'reporte_arriendos.html', {'arriendos': arriendos})