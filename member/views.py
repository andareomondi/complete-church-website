from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
# Create your views here.

# authentication views
class Login(View):
     def post(self, request):
        user = Member()
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=username, password=password)
        if user is not None:
            login(request, user)
            data = {
                'redirect':'/',
                'status': 'success',
                'message': 'Login successful',
            }
            return JsonResponse(data)
        else:
            data = {
                'status': 'error',
                'message': 'Invalid login credentials'
            }
            return JsonResponse(data)

class Register(View):
     def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2:
            data = {
                'status': 'error',
                'message': 'Passwords do not match'
            }
            return JsonResponse(data)
        else:
            user = Member.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name, phone_number=phone_number)
            user.save()
            data = {
                'redirect': '/',
                'status': 'success',
                'message': 'User registered successfully'
            }
            return JsonResponse(data)

class SignOut(View):
    def get(self, request):
        logout(request)
        return redirect(to='home')

# Important views handled here for the app
class Home(View):
    def get(self, request):
        return render(request, 'member/home.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name='member/about.html')

# specific views for specific sections
class Word(View):
	def get(self, request):
		words = Sermon.objects.all()
		context = {
			'words': words,
		}
		return render(request, 'member/sermons.html', context=context)

class PrayerCells(View):
     def get(self, request):
          return render(request, 'member/prayercells.html')
class Profile(View):
        def get(self, request, pk):
            if request.user.is_authenticated:
                user = Member.objects.get(id=pk)
                context = {
                    'user': user,
                }
                return render(request, 'member/profile.html', context=context)
            else:
                return redirect(to='login')
class Gallery(View):
    def get(self, request):
        images = ChurchImage.objects.all()
        context = {
            'images':images,
        }
        return render(request, template_name='member/gallery.html', context=context)

class SundaySchool(View):
     def get(self, request):
          return render(request, 'member/sundayschool.html')

class CEDGroups(View):
     def get(self, request):
          groups = CedGroup.objects.all()
          context = {
               'groups': groups
          }
          return render(request, 'member/cedgroups.html', context = context)
class SpecificCedGroup(View):
     def get(self, request, pk):
        group = CedGroup.objects.get(id=pk)
        practice = group.cedpracticeday_set.all()
        context = {
            'cedgroup': group,
            'practice': practice,
        }
        return render(request, 'member/cedgroup.html', context=context)
