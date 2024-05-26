from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from .models import Contact


def contact(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            tg_username = request.POST.get('tg_username')
            Contact.objects.create(
                phone=phone,
                name=name,
                tg_username=tg_username
            )
            messages.success(request, 'Xabaringiz muvaffaqiyatli yuborildi!')
            return redirect('contact')
        return render(request, 'contact.html', {'success': False})
    except Exception as e:
        messages.error(request, 'Xatolik yuz berdi: ' + str(e))
        return render(request, 'contact.html', {'success': False})
