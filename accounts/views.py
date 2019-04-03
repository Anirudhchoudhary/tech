from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect ,reverse
from django.views.generic import FormView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


from .forms import RegisterForm,Login_form

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data.get('email')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(email=email, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'accounts/signup.html', {'form': form})


# class LoginView(FormView):
#     form_class = Login_form
#     template_name = 'accounts/login.html'
#     success_url = '/'

#     def form_valid(self , form):
#         email = form.cleaned_data.get('email')
#         password = form.cleaned_data.get('password')
#         user = authenticate(self.request , email = email, password = password)
#         if user is not None:
#             if not user.is_active:
#                 messages.error(self.request , "This User is not active")
#             login(self.request , user)   
#         else:
#             messages.error(self.request  , "Check Your Details")
#         return super(LoginView , self).form_invalid(form)  

# def logout_user(request):
#     logout(request)
#     return reverse_lazy('')

class LoginView(FormView):
    form_class = Login_form
    template_name = 'accounts/login.html'
    success_url = '/'

    def form_valid(self , form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(self.request , email = email , password = password)
        print(user)
        if user is not None:
            if not user.is_active:
                messages.error(self.request , "This User is not active")
            login(self.request , user)        
        else:
            messages.error(self.request  , "Check Your Details")
        return super(LoginView , self).form_invalid(form)   

    # def get_success_url(self,**kwargs):
    #     super(LoginView , self).get_success_url(**kwargs)
    #     success_url = reverse("items:list")
    #     return success_url 

     

 

def logout_user(request):
    logout(request)
    return redirect('home') 

class SignUp(SuccessMessageMixin,CreateView):
    form_class = RegisterForm
    success_url = '/'
    success_message = 'Conformation mail has been send to your email conform and login'
    template_name = 'accounts/signup.html'

    def get_success_url(self,**kwargs):
        super(SignUp , self).get_success_url(**kwargs)
        success_url = reverse("accounts:login")
        return success_url 