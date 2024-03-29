from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
# Create your views here.

class UserNameValidationView(View):
    def post(self, request):
        data = json.leads(request.body)
        username=data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric character'})
        
        return JsonResponse({'username_valid', True})

class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')