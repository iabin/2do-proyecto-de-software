from django.contrib.auth import login
from django.http import HttpResponse
from aplicacion.models import Profile, Course, Take
from aplicacion.serializers import UserSerializer, CourseSerializer, TakeSerializer
from rest_framework import generics
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import login, authenticate
from aplicacion.forms import SignUpForm, CrearClaseForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import DetailView


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class TakeList(generics.ListCreateAPIView):
    queryset = Take.objects.all()
    serializer_class = TakeSerializer


class TakeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Take.objects.all()
    serializer_class = TakeSerializer


#def signup(request):
    #if request.method == 'POST':
     #   form = SignUpForm(request.POST)
      #  if form.is_valid():
            # este form save, guarda en la base, solo es eso
            # form.save(commit=False)
       #     form.save()
        #    return redirect('signup')
    #else:
     #   form = SignUpForm()
    #return render(request, 'signup.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def logout_view(request):
    logout(request)
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')


def busca(request):
    toSearch = request.GET['busqueda']
    if not toSearch:
        return HttpResponse("return this string")

    searchResult = Course.objects.filter(title__icontains=toSearch)
    return render(request, 'resultados.html', {'resultados': searchResult})

class CourseDetailView(DetailView):
    model = Course

class UserDetailView(DetailView):
    model = User

@login_required
def crearClase(request):
    form = CrearClaseForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            current_user = request.user
            new_teacher = form.save(commit=False)
            usuario = current_user.profile
            new_teacher.teacher = usuario
            new_teacher.save()
            messages.success(request, 'Clase creada exitosamente')
            return redirect('crearClase')
        else:
            form = CrearClaseForm()
    return render(request, 'crearClase.html', {'form': form})


# Create your views here.
