from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactUsForm
from .models import ContactUs
from .tasks import contact_us_form


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title', )
            email_from = form.cleaned_data.get('email_from', )
            text = form.cleaned_data.get('message', )
            message = ('{}: {}'.format(email_from, text))
            email_from = form.cleaned_data.get('email_from', )
            email_to = ['moyshedev@gmail.com', 'shatoon2@gmail.com', 'chicshinestore@gmail.com']

            contact_us_form.delay(title=title, message=message, email_from=email_from, email_to=email_to)
            # Added email to the database
            email = ContactUs.objects.create(title=title, message=message, email_from=email_from, email_to=email_to)

            if email:
                messages.success(request, 'Success: Sent email from {}!'.format(email_from))
                return redirect('contact-us')
            else:
                messages.error(request, 'Email sending error!')
        else:
            messages.error(request, 'Please enter correct data in the form fields!')
    else:
        form = ContactUsForm()
    return render(request, 'contact_us/contact_us.html', {'form': form})
