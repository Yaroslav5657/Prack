from django.shortcuts import render
from django.http import HttpResponse
import random

def captcha_form(request):
    if request.method == 'POST':
        captcha_input = request.POST.get('captcha_input')
        captcha_number = request.POST.get('captcha_number')
        if captcha_input == captcha_number:
            return HttpResponse("CAPTCHA введено вірно!")
        else:
            return HttpResponse("Неправильний CAPTCHA. Спробуйте ще раз.")
    else:
        captcha_number = random.randint(1000, 9999)
        return render(request, 'index.html', {'captcha_number': captcha_number})