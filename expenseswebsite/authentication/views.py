from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage


# Create your views here.

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')



    def post(self, request):

        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        
        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'Password too short')
                    return render(request, 'authentication/register.html', context)
                
                user= User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.is_active = False
                user.save()
                
                email_body = 'Test body'
                emai_subject = "Activate your account"
                email=EmailMessage(
                    emai_subject,
                    email_body,
                    'donotreply@semicolon.com',
                    [email],
                  
                )
                email.send(fail_silently=False)
                messages.success(request, 'Account Successfuly created')
                return render(request, 'authentication/register.html')
        return render(request, 'authentication/register.html')



    # def post(self, request):
    #     messages.success(request, "Success")
        
    #     messages.warning(request, "Warning")
    #     messages.info(request, "Info")
    #     messages.error(request, "Error")
    #     return render(request, 'authentication/register.html')

class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric characters'}, status=400)
        return JsonResponse({'username_valid': True})

        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Sorry Username name already in use'}, status=409)
        return JsonResponse({'username_valid': True})   
      

class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']

        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is Invalid'}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Sorry email name already in use'}, status=409)
        return JsonResponse({'email_valid': True})   


# class VerificationView(View):
#     def get(self, request, uidb64, token):
#         return redirect('Login')
