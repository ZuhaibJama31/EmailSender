# emailsender/views.py
from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailForm

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            to_email = form.cleaned_data['Email']
            subject = form.cleaned_data['Subject']
            message = form.cleaned_data['Message']
            send_mail(subject, message, 'techwarsame@gmail.com', [to_email])
            return render(request, 'emailsender/success.html')
    else:
        form = EmailForm()
    return render(request, 'emailsender/email_form.html', {'form': form})
