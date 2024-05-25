from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from .models import Contact


def contact(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            Contact.objects.create(
                subject=subject,
                name=name, email=email, message=message
            )
            messages.success(request, 'Xabaringiz muvaffaqiyatli yuborildi!')
            return redirect('contact')
        return render(request, 'contact.html', {'success': False})
    except Exception as e:
        messages.error(request, 'Failed to send message')
        return render(request, 'contact.html', {'success': False})
